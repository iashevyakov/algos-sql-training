def time_for_copy_without_first(x: int, y: int, n: int) -> int:
    left = 0
    right = (n - 1) * max(x, y)

    while left + 1 < right:
        middle = (left + right) // 2
        if middle / x + middle / y < n - 1:
            left = middle
        else:
            right = middle
    return right

x, y = map(int, input().split())
n = int(input())
time_without_first = time_for_copy_without_first(x, y, n)
print(time_without_first + min(x, y))
