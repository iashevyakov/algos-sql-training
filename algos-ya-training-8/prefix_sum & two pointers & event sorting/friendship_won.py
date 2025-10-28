def get_friendship_win_condition(n: int, a: list[int]) -> tuple[int, int, int]:
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    min_diff = prefix_sum[n]
    best_l, best_r = 1, n

    for left in range(1, n):
        sd_v = prefix_sum[left]
        best_diff_for_left = prefix_sum[n]
        best_right_for_left = left + 1
        left_r, right_r = left + 1, n

        while left_r <= right_r:
            mid_right = (left_r + right_r) // 2
            sd_m = prefix_sum[n] - prefix_sum[mid_right - 1]
            diff = abs(sd_v - sd_m)
            if sd_m < sd_v:
                right_r = mid_right - 1
            else:
                left_r = mid_right + 1

            if diff < best_diff_for_left:
                best_diff_for_left = diff
                best_right_for_left = mid_right

        if best_diff_for_left < min_diff:
            best_l, best_r = left, best_right_for_left
            min_diff = best_diff_for_left

    return min_diff, best_l, best_r


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*get_friendship_win_condition(n, a))
