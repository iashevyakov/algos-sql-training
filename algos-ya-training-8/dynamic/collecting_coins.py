def get_max_coins(n: int, way: list[str]) -> int:
    dp = []
    inf = float('-inf')
    for i in range(n):
        row = []
        for j in range(3):
            if way[i][j] == 'C':
                row.append(1)
            elif way[i][j] == '.':
                row.append(0)
            else:
                row.append(inf)
        dp.append(row)

    for i in range(1, n):
        for j in range(3):
            first_value = dp[i - 1][j]
            second_value = dp[i - 1][j + 1] if j + 1 < 3 else inf
            third_value = dp[i - 1][j - 1] if j - 1 >= 0 else inf
            dp[i][j] += max(first_value, second_value, third_value)
        if all(dp[i][j] == inf for j in range(3)):
            return max(max(dp[i - 1]), 0)
    return max(max(dp[n - 1]), 0)


if __name__ == "__main__":
    n = int(input())
    way = [input() for _ in range(n)]
    print(get_max_coins(n, way))
