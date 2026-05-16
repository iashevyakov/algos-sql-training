"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/search-in-depth
"""
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)


def bfs(root: int, graph: dict[int, set], visited: set[int], answer: list[int]):
    edge_vertices = graph[root]
    for v in edge_vertices:
        if v not in visited:
            answer.append(v)
            visited.add(v)
            bfs(v, graph, visited, answer)


def main():
    n, m = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        if u != v:
            graph[u].add(v)
            graph[v].add(u)

    visited, answer = {1}, [1]
    bfs(1, graph, visited, answer)
    print(len(answer))
    print(*sorted(answer))


if __name__ == '__main__':
    main()
