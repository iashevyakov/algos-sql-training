"""
https://coderun.yandex.ru/selections/yandex-interview/problems/interesting-journey
"""
from queue import Queue


def distance(p1: tuple[int, ...], p2: tuple[int, ...]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_min_road_cnt(
    points: list[tuple[int, ...]], n: int, k: int, src: int, dst: int
) -> int:
    q = Queue()
    q.put(src)
    distances = {src: 0}
    while not q.empty():
        cur_city = q.get()
        if cur_city == dst:
            return distances[cur_city]
        for city in range(n):
            if city not in distances:
                dist = distance(points[city], points[cur_city])
                if dist <= k:
                    q.put(city)
                    distances[city] = distances[cur_city] + 1
    return -1


def main():
    n = int(input())
    points = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    k = int(input())
    src, dst = map(lambda num: num - 1, map(int, input().split()))

    min_road_cnt = get_min_road_cnt(points, n, k, src, dst)
    return min_road_cnt


if __name__ == '__main__':
    print(main())
