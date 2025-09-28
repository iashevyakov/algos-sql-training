n = int(input())
numbers = tuple(map(int, input().split()))

first, second = numbers[n - 2], numbers[n - 1]
min_diff = numbers[n - 1] - numbers[n - 2]

for i in range(n - 2, 0, -1):
    diff = numbers[i] - numbers[i - 1]
    if diff <= min_diff:
        min_diff = diff
        first, second = numbers[i - 1], numbers[i]

print(first, second)
