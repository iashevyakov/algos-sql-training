def get_min_swim_cnt(s: str) -> int:
    n = len(s)
    dp = [[-1] * (n + 1), [-1] * (n + 1)]
    dp[0][0], dp[1][0] = 0, 1
    left_confs, right_confs = {'L', 'B'}, {'R', 'B'}
    for i in range(1, n + 1):
        ch = s[i - 1]
        left_conf_swim = int(ch in left_confs)
        right_conf_swim = int(ch in right_confs)
        dp[0][i] = min(
            dp[0][i - 1] + left_conf_swim,
            dp[1][i - 1] + right_conf_swim + 1
        )
        dp[1][i] = min(
            dp[1][i - 1] + right_conf_swim,
            dp[0][i - 1] + left_conf_swim + 1
        )
    return dp[1][n]


if __name__ == "__main__":
    s = input()
    print(get_min_swim_cnt(s))
