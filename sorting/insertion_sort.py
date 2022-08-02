from typing import List


def insertion_sort(nums: List[int]) -> None:
    for i in range(1, len(nums)):
        for j in reversed(range(1, i)):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
