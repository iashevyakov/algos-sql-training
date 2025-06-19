def search_position(n: int, numbers: list[int], target: int) -> int:
    left, right = 0, n - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return left


n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

print(search_position(n, numbers, target))
