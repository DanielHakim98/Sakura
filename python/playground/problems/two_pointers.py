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


def main():
    # print(squares_sorted_array([-4, -1, 0, 3, 10]))
    print(threesum([-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    main()
