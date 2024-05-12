from dataclasses import dataclass
import json
import sys
from typing import Any

import requests
from requests import Response
from requests.exceptions import Timeout, JSONDecodeError, HTTPError


def fetch_data_gov_my(url: str, query_params: dict[str, str]) -> Response:
    response = None
    max_retry = 3
    retry = 0
    while retry < max_retry:
        try:
            response = requests.get(url, params=query_params)
            response.raise_for_status()
        except Timeout as e:
            print(e, file=sys.stderr)
            print(f"Attempt retry #{retry}...", file=sys.stderr)
            retry += 1
        except HTTPError as e:
            print(e, file=sys.stderr)
            return response
        else:
            return response

    if retry >= max_retry:
        raise Timeout(f"Max retries exceed limit '{max_retry}'")


def get_res_body(response: Response) -> Any:
    res_body = []
    try:
        res_body = response.json()
    except JSONDecodeError as e:
        print("JSON decode error:", e, file=sys.stderr)
    return res_body


@dataclass
class RidershipStats:
    average_ridership_per_k: float
    k: int
    data: list[dict[str, Any]]


def max_average_ridership(
    body_data: list[dict[str, Any]], win_size: int
) -> RidershipStats:
    win_sum = 0
    max_sum = 0

    for item in body_data:
        win_sum += item["rail_lrt_kj"]

    max_sum = win_sum
    max_win_range = (0, win_size)

    for win_end in range(win_size, len(body_data)):
        out_win = body_data[win_end - win_size]
        in_win = body_data[win_end]

        win_sum = win_sum - out_win["rail_lrt_kj"] + in_win["rail_lrt_kj"]
        if win_sum > max_sum:
            max_sum = win_sum
            max_win_range = (win_end - win_size + 1, win_end + 1)

    return RidershipStats(
        max_sum / win_size, win_size, body_data[max_win_range[0] : max_win_range[1]]
    )


if __name__ == "__main__":
    params = {
        "id": "ridership_headline",
        "date_start": "2019-01-01@date",
        "date_end": "2024-05-01@date",
    }
    response = fetch_data_gov_my("https://api.data.gov.my/data-catalogue/", params)
    body_data = get_res_body(response)
    res = max_average_ridership(body_data, 7)
    print(json.dumps(res.data))
