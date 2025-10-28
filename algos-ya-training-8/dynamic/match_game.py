def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_dp_last_elem(n: int) -> int:
    dp = [False] * (n + 1)
    dp[0] = False

    for i in range(1, n + 1):
        dp[i] = False
        for match_move in [1, 2, 3]:
            if i >= match_move:
                match_remain = i - match_move
                if not is_prime(match_remain) and not dp[match_remain]:
                    dp[i] = True
                    break
    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(1 if get_dp_last_elem(n) else 2)
