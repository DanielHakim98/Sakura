import json
import random
import sys
import time
import asyncio
from typing import Any
from dataclasses import dataclass

import requests
from requests import Response
from requests.exceptions import Timeout, HTTPError, JSONDecodeError


def retry_backoff(prev_retry: int) -> int:
    current_retry = prev_retry + 1
    sleep = 2 ** (current_retry) + random.uniform(0, 1)
    print(f"Attempt retry #{current_retry} in {sleep} second(s)", file=sys.stderr)
    time.sleep(sleep)
    return current_retry


def fetch_data_gov_my(url: str, params: dict[str, str]) -> Response:
    response = None
    max_retry = 3
    retry = 0
    status_code = 0
    while retry < max_retry:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()

        except HTTPError as e:
            print(e, file=sys.stderr)

            status_code = e.response.status_code
            if status_code != 429:
                return response

            retry = retry_backoff(retry)

        except Timeout as e:
            print(e, file=sys.stderr)
            retry = retry_backoff(retry)

        else:
            return response

    if retry >= max_retry:
        if status_code == 429:
            raise HTTPError("Rate limit exceeded and retries exhausted")
        raise Timeout(f"Max retries exceeded limit '{max_retry}'.")


url = "https://api.data.gov.my/data-catalogue/"
query_param_years = [
    {
        "id": "ridership_headline",
        "date_start": "2019-01-01@date",
        "date_end": "2019-12-31@date",
    },
    {
        "id": "ridership_headline",
        "date_start": "2020-01-01@date",
        "date_end": "2020-12-31@date",
    },
    {
        "id": "ridership_headline",
        "date_start": "2021-01-01@date",
        "date_end": "2021-12-31@date",
    },
]


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


async def main():
    responses = await asyncio.gather(
        *[
            asyncio.to_thread(fetch_data_gov_my, url, parameter)
            for parameter in query_param_years
        ]
    )
    json_results = [get_res_body(res) for res in responses]
    max_aver_rideship_by_year = [max_average_ridership(res, 7) for res in json_results]
    for final in max_aver_rideship_by_year:
        print(json.dumps(final.data))


if __name__ == "__main__":
    asyncio.run(main())
