def squares_sorted_array(nums: list[int]):
    result = [0] * len(nums)
    right_pointer = len(nums) - 1
    left_pointer = 0
    current_idx = len(nums) - 1
    while left_pointer <= right_pointer:
        left_val = abs(nums[left_pointer])
        right_val = abs(nums[right_pointer])
        if left_val > right_val:
            result[current_idx] = left_val * left_val
            left_pointer += 1
        else:
            result[current_idx] = right_val * right_val
            right_pointer -= 1
        current_idx -= 1
    return result


def threesum(nums: list[int]):
    nums.sort()
    result = []
    return result


def two_sum_2(nums: list[int], target: int):
    left = 0
    right = len(nums) - 1

    while left < right:
        left_val = nums[left]
        right_val = nums[right]

        if left_val + right_val > target:
            right -= 1
        elif left_val + right_val < target:
            left += 1
        else:
            return [left + 1, right + 1]


def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int):
    if m == 0:
        nums1[0:] = nums2[0:]
        return
    if n == 0:
        return

    current_pointer = m + n - 1
    pointer_1 = m - 1
    pointer_2 = n - 1

    while current_pointer >= 0 and pointer_2 >= 0:
        if pointer_1 < 0:
            nums1[current_pointer] = nums2[pointer_2]
            pointer_2 -= 1
            current_pointer -= 1
            continue
        if nums2[pointer_2] > nums1[pointer_1]:
            nums1[current_pointer] = nums2[pointer_2]
            pointer_2 -= 1
        else:
            nums1[current_pointer] = nums1[pointer_1]
            pointer_1 -= 1
        current_pointer -= 1


def valid_palindrome_2(s: str) -> bool:
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        left_val, right_val = s[left_pointer], s[right_pointer]
        if left_val != right_val:
            s_exclude_left = s[left_pointer + 1 : right_pointer + 1]
            s_exclude_right = s[left_pointer:right_pointer]

            return (
                s_exclude_left == s_exclude_left[::-1]
                or s_exclude_right == s_exclude_right[::-1]
            )
        left_pointer += 1
        right_pointer -= 1

    return True


def move_zeroes(nums: list[int]) -> None:
    total_zero = 0
    left_pointer = 0
    for pointer in range(len(nums)):
        if nums[pointer] == 0:
            total_zero += 1
        else:
            nums[left_pointer] = nums[pointer]
            left_pointer += 1
    for idx in range(len(nums) - total_zero, len(nums)):
        nums[idx] = 0


def max_area(heights: list[int]) -> int:
    max_area = min(heights[0], heights[1]) * (1 - 0)
    start, end = 0, 1
    for cur in range(2, len(heights)):
        cmp_end = min(heights[cur], heights[end]) * (cur - end)
        cmp_start = min(heights[cur], heights[start]) * (cur - start)

        if cmp_end >= cmp_start:
            if cmp_end > max_area:
                max_area = cmp_end
                start = end
                end = cur
        else:
            if cmp_start > max_area:
                max_area = cmp_start
                end = cur
    return max_area


def main():
    print(max_area([2, 3, 10, 5, 7, 8, 9]))
    # print(squares_sorted_array([-4, -1, 0, 3, 10]))
    # print(threesum([-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    main()
