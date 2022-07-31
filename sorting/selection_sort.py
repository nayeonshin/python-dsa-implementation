from typing import List


def selection_sort(nums: List[int]) -> None:
    """
    Time complexity: O(n^2) where n is len(nums)
    """
    for i in range(len(nums) - 1):
        min_value_index = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_value_index]:
                min_value_index = j

        nums[i], nums[min_value_index] = nums[min_value_index], nums[i]
