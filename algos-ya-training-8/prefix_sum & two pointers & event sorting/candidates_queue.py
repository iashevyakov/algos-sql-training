def get_prefix_sum(n: int, m: int, a: tuple[int, ...], x: int) -> list[int]:
    prefix_sum = [0] * (n + m + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + int(a[i - 1] >= x)
    return prefix_sum


if __name__ == '__main__':
    n, x = map(int, input().split())
    a = tuple(map(int, input().split()))
    m = int(input())
    prefix_sum = get_prefix_sum(n, m, a, x)
    left, right = 0, len(a)
    for _ in range(m):
        req = list(map(int, input().split()))
        req_type = req[0]
        if req_type == 2:
            left += 1
        elif req_type == 1:
            new_a = req[1]
            right += 1
            prefix_sum[right] = prefix_sum[right - 1] + int(new_a >= x)
        else:
            k = req[1]
            print(prefix_sum[left + k] - prefix_sum[left])
