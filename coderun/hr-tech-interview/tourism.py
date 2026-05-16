"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/tourism
"""


def main():
    n = int(input())
    points = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    prefix_sum_right = [0] * (n + 1)
    prefix_sum_left = [0] * (n + 1)
    for i in range(2, n + 1):
        prefix_sum_right[i] = prefix_sum_right[i - 1] + max(points[i - 1][1] - points[i - 2][1], 0)
        prefix_sum_left[i] = prefix_sum_left[i - 1] + max(points[i - 2][1] - points[i - 1][1], 0)

    m = int(input())
    for _ in range(m):
        track_start, track_end = map(int, input().split())
        if track_start <= track_end:
            rise = prefix_sum_right[track_end] - prefix_sum_right[track_start]
        else:
            rise = prefix_sum_left[track_start] - prefix_sum_left[track_end]
        print(rise)


if __name__ == '__main__':
    main()
