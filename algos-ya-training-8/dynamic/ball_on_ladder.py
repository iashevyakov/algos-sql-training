def ball_routes_cnt(n: int) -> int:
    dp = [-1] * (n + 3)
    dp[n + 2] = 0
    dp[n + 1] = 0
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1] + dp[i + 2] + dp[i + 3]
    return dp[0]


if __name__ == "__main__":
    n = int(input())
    print(ball_routes_cnt(n))
