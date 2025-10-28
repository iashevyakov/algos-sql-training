from collections import defaultdict
from queue import Queue


def get_stalemates_route_min_len(n: int, adj: defaultdict[int, list[int]]) -> int:
    distances, source_vertices = {}, {}
    queue = Queue()

    for v in range(1, n + 1):
        if len(adj[v]) == 1:
            distances[v], source_vertices[v] = 0, v
            queue.put(v)
        else:
            distances[v] = None

    while queue:
        current_v = queue.get()
        for neighbour in adj[current_v]:
            if distances[neighbour] is None:
                distances[neighbour] = distances[current_v] + 1
                source_vertices[neighbour] = source_vertices[current_v]
                queue.put(neighbour)
            elif source_vertices[neighbour] != source_vertices[current_v]:
                return distances[current_v] + distances[neighbour] + 1


if __name__ == "__main__":
    n = int(input().strip())
    adj = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    print(get_stalemates_route_min_len(n, adj))
