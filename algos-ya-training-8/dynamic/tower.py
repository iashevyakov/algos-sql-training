def get_tower_safety(a: list[int], begin: int, end: int) -> int:
    tower_heights = a[begin:end]
    tower_heights_sum = sum(tower_heights)
    tower_heights_min = min(tower_heights)
    tower_safety = tower_heights_sum * tower_heights_min
    return tower_safety


def get_max_fortress_safety(n: int, k: int, a: list[int]) -> tuple[int, list[int]]:
    prev = [-1] * (n + 1)
    dp = [0] * (n + 1)
    for i in range(k, n + 1):
        for j in range(i - k + 1):
            tower_begin = j
            tower_end = j + k
            tower_safety = get_tower_safety(a, tower_begin, tower_end)

            cur_tower_safety = dp[tower_begin] + tower_safety
            if cur_tower_safety > dp[i]:
                dp[i] = cur_tower_safety
                prev[i] = tower_begin

    ans = []
    i = n
    while i > 0 and prev[i] != -1:
        ans.append(prev[i] + 1)
        i = prev[i]

    ans.reverse()
    return len(ans), ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q, towers_begins = get_max_fortress_safety(n, k, a)
    print(q)
    print(*towers_begins)
