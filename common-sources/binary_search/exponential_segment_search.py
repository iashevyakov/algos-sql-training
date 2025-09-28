def exponential_segment_search(nums: list[int], target: int) -> tuple[int, int]:
    border = 1
    if nums[0] == target:
        return 0, border
    last = len(nums) - 1
    while border < last and nums[border] < target:
        border *= 2
    return border // 2, min(border, last)

n = int(input())
nums = list(map(int, input().split()))
target = int(input())
print(*exponential_segment_search(nums, target))
