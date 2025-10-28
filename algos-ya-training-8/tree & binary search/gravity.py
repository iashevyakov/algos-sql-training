from bisect import bisect_right


def get_particle_gravity(n: int, a: list[int], m: int, b: list[int]) -> int:
    a_sorted, b_sorted = sorted(a), sorted(b)
    prefix_sum_a = [0] * (n + 1)
    prefix_sum_b = [0] * (m + 1)
    for i in range(n):
        prefix_sum_a[i + 1] = prefix_sum_a[i] + a_sorted[i]
    for i in range(m):
        prefix_sum_b[i + 1] = prefix_sum_b[i] + b_sorted[i]

    answer = 0

    for i in range(n):
        pos = bisect_right(b_sorted, a[i])
        sum_1 = a[i] * pos - prefix_sum_b[pos]
        sum_2 = prefix_sum_b[m] - prefix_sum_b[pos] - a[i] * (m - pos)
        answer += i * (sum_1 + sum_2)

    for j in range(m):
        pos = bisect_right(a_sorted, b[j])
        sum_1 = b[j] * pos - prefix_sum_a[pos]
        sum_2 = prefix_sum_a[n] - prefix_sum_a[pos] - b[j] * (n - pos)
        answer -= j * (sum_1 + sum_2)

    return answer


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    print(get_particle_gravity(n, a, m, b))
