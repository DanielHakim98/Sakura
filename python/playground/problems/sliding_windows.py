import sys


def max_average_of_k_window(in_list: list[int], k: int) -> list[float | int]:
    current_sum = 0
    for i in range(k):
        current_sum += in_list[i]
    max_average = current_sum / k

    for idx in range(k, len(in_list)):
        removed_element = in_list[idx - k]
        added_element = in_list[idx]

        current_sum = current_sum + added_element - removed_element
        current_average = current_sum / k

        if current_average > max_average:
            max_average = current_average

    return max_average


def smallest_subarray(arr: list[int], s: int) -> int:
    win_start = 0
    win_sum = 0
    min_length = sys.maxsize

    for win_size in range(len(arr)):
        win_sum += arr[win_size]
        while win_sum >= s:
            win_length = win_size - win_start + 1
            min_length = win_length if win_length < min_length else min_length
            win_sum -= arr[win_start]
            win_start += 1

    return 0 if min_length == sys.maxsize else min_length


def longest_substring_distinct_k(string: str, max_unique: int) -> int:
    win_start = 0
    max_length = 0
    unique_chars = {}

    for win_end, char in enumerate(string):
        unique_chars[char] = unique_chars.get(char, 0) + 1

        while len(unique_chars) > max_unique:
            char_at_win_start = string[win_start]
            unique_chars[char_at_win_start] = unique_chars.get(char_at_win_start, 0) - 1
            if unique_chars[char_at_win_start] == 0:
                del unique_chars[char_at_win_start]

            win_start += 1

        win_length = win_end - win_start + 1
        max_length = win_length if win_length > max_length else max_length

    return max_length


def longest_non_repeat(string: str) -> int:
    win_start = 0
    max_length = 0
    unique_chars = {}

    for win_end, char in enumerate(string):
        if char in unique_chars:
            char_count = unique_chars.get(char) + 1
            win_start = char_count if char_count > win_start else win_start

        unique_chars[char] = win_end
        win_length = win_end - win_start + 1
        max_length = win_length if win_length > max_length else max_length

    return max_length


def longest_repeat_char_replace(string: str, k: int) -> int:
    win_start = 0
    max_length = 0
    unique_chars = {}
    most_frequent_char = 0

    for win_end, char in enumerate(string):
        unique_chars[char] = unique_chars.get(char, 0) + 1
        current_char_count = unique_chars.get(char)
        most_frequent_char = (
            current_char_count
            if current_char_count > most_frequent_char
            else most_frequent_char
        )

        letter_to_replace = (win_end - win_start + 1) - most_frequent_char
        while letter_to_replace > k:
            char_win_at_start = string[win_start]
            unique_chars[char_win_at_start] = unique_chars.get(char_win_at_start) - 1
            if unique_chars.get(char_win_at_start) < 1:
                del unique_chars[char_win_at_start]
            win_start += 1
            letter_to_replace = (win_end - win_start + 1) - most_frequent_char

        win_length = win_end - win_start + 1
        max_length = win_length if win_length > max_length else max_length

    return max_length


def contain_duplicate_2(nums: list[int], k: int) -> bool:
    unique = {}
    start_win = 0
    for end_win in range(len(nums)):
        if end_win - start_win > k:
            del unique[nums[start_win]]
            start_win += 1

        if nums[end_win] in unique:
            return True

        unique[nums[end_win]] = {}

    return False


if __name__ == "__main__":
    # print(longest_substring_distinct_k("araaci", 1))
    contain_duplicate_2([1, 0, 1, 1], 1)
