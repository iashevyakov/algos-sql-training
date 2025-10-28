from bisect import bisect_left


def get_nameplate_ids(n: int, p: int, c: list[int]) -> tuple[int, int]:
    sorted_nums_with_idx = sorted((c[i], i + 1) for i in range(n))
    sorted_nums = [c[0] for c in sorted_nums_with_idx]
    min_rate_diff = float('inf')
    ans_i, ans_j = 1, 2

    for i in range(n):
        cur_num, cur_num_idx = sorted_nums_with_idx[i]
        target = cur_num / p
        left, right = 0, n - 1
        supposed_j = bisect_left(sorted_nums, target, left, right)

        for j in range(max(0, supposed_j - 1), min(n, supposed_j + 2)):
            if j != i:
                second_num, second_num_idx = sorted_nums_with_idx[j]
                if second_num:
                    rate_diff = abs(cur_num / second_num - p)
                    if rate_diff < min_rate_diff:
                        min_rate_diff = rate_diff
                        ans_i, ans_j = cur_num_idx, second_num_idx
    return ans_i, ans_j


if __name__ == '__main__':
    n, p = map(int, input().split())
    c = list(map(int, input().split()))
    print(*get_nameplate_ids(n, p, c))
