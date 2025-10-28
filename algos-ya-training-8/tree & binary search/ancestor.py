import sys

from collections import defaultdict

sys.setrecursionlimit(100000000)


def dfs(node: int, t: int):
    node_start = t + 1
    node_end = node_start

    for child in children[node]:
        child_start, node_end = dfs(child, node_end)

    times[node] = node_start, node_end
    return node_start, node_end


n = int(input())
ps = map(int, input().split())
root = -1
children = defaultdict(list)

for i, p in enumerate(ps, start=1):
    if p:
        children[p].append(i)
    else:
        root = i

times = {}
dfs(root, 0)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    a_time = times[a]
    b_time = times[b]
    is_ancestor = b_time[0] >= a_time[0] and b_time[1] <= a_time[1]
    print(int(is_ancestor))
