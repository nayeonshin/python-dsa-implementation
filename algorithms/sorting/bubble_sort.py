from typing import List


def bubble_sort(nums: List[int]) -> None:
    """
    Time complexity: O(n^2) where n is len(nums)
    """
    for i in reversed(range(1, len(nums))):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def short_bubble(nums: List[int]) -> None:
    for i in reversed(range(1, len(nums))):
        has_swapped = False

        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                has_swapped = True

        if not has_swapped:
            break


"""
추가 최적화

이전 패스에서 앞뒤 자리 비교(swap)가 있었는지 여부를 체크하는 대신 마지막으로 앞뒤 자리 비교가 있었던 index를 기억해두면
다음 패스에서는 그 자리 전까지만 정렬해도 됨. 따라서 한 칸씩 정렬 범위를 줄여나가는 대신 한번에 여러 칸씩 정렬 범위를 줄여나갈 수 있음.
"""


def optimized_bubble_sort(nums: List[int]) -> None:
    end = len(nums) - 1

    while end > 0:
        last_swap = 0

        for i in range(end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                last_swap = i

        end = last_swap
