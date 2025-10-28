def num_after_seconds(n: int, k: int) -> int:
    if k == 0:
        return n
    last_digit = n % 10
    if last_digit == 5:
        return n + 5
    if last_digit == 0:
        return n
    special_odd_nums = {1, 3, 7, 9}
    if last_digit in special_odd_nums:
        n += last_digit
        k -= 1
        last_digit = n % 10
    n += (k // 4) * 20
    values = {
        2: {0: 0, 1: 2, 2: 2 + 4, 3: 2 + 4 + 8},
        4: {0: 0, 1: 4, 2: 4 + 8, 3: 4 + 8 + 6},
        6: {0: 0, 1: 6, 2: 6 + 2, 3: 6 + 2 + 4},
        8: {0: 0, 1: 8, 2: 8 + 6, 3: 8 + 6 + 2}
    }
    n += values[last_digit][k % 4]
    return n


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(num_after_seconds(n, k))
