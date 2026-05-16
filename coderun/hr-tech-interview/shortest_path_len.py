"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/shortest-path-length
"""

from collections import defaultdict
from queue import Queue


def bfs(src: int, dst: int, edges: dict[int, list[int]]) -> int:
    q = Queue()
    q.put(src)
    distances = {src: 0}

    while not q.empty():
        v = q.get()
        if v == dst:
            return distances[v]
        childs = edges[v]
        for child in childs:
            if child not in distances:
                distances[child] = distances[v] + 1
                q.put(child)

    return -1


def main():
    n = int(input())
    edges = defaultdict(list)
    for v1 in range(1, n + 1):
        v1_edges = map(int, input().split())
        for v2, edge_existence in enumerate(v1_edges, start=1):
            if edge_existence:
                edges[v1].append(v2)

    src, dst = map(int, input().split())
    print(bfs(src, dst, edges))


if __name__ == '__main__':
    main()
