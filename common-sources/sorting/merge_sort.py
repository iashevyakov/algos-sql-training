_ = int(input())
nums = list(map(int, input().split()))


def merge(left: list[int], right: list[int]) -> list[int]:
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    for k in range(i, len(left)):
        merged.append(left[k])
    for k in range(j, len(right)):
        merged.append(right[k])
    return merged


def merge_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    if n < 2:
        return nums
    mid = n // 2
    left = nums[0:mid]
    right = nums[mid:n]
    return merge(merge_sort(left), merge_sort(right))


print(*merge_sort(nums))
