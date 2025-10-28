from bisect import bisect_right


def get_intervals_subset_max_weight(n: int, data: list[tuple[float, float, float]]) -> float:
    if n == 0:
        return 0
    data.sort(key=lambda interval: interval[1])
    dp = [interval[2] for interval in data]
    intervals_ends = [interval[1] for interval in data]
    for i in range(1, n):
        bi, ei, wi = data[i]
        left_nearest = bisect_right(intervals_ends, bi) - 1
        if left_nearest != -1:
            dp[i] += dp[left_nearest]
        dp[i] = max(dp[i - 1], dp[i])
    return max(dp)


if __name__ == "__main__":
    n = int(input())
    data = []
    for _ in range(n):
        b, e, w = map(float, input().split())
        data.append((b, e, w))
    print(get_intervals_subset_max_weight(n, data))
