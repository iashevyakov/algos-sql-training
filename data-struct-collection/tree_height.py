import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


def get_tree_height(tree: dict, root: int) -> int:
    childs = tree[root]
    max_child_height = 0
    for child in childs:
        child_height = get_tree_height(tree, child)
        max_child_height = max(max_child_height, child_height)
    return max_child_height + 1


if __name__ == "__main__":
    n = int(input())
    tree = defaultdict(list)
    parents = map(int, input().split())
    root = None
    for v, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(v)
        else:
            root = v
    height = get_tree_height(tree, root)
    print(height)
