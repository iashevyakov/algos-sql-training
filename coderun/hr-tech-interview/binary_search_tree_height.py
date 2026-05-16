"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/tree-height
"""
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value: int, heights: dict[int, int]):
        node = self
        while True:
            if value > node.value:
                child = node.right
                if child is None:
                    new_node = Node(value)
                    node.right = new_node
                    heights[value] = heights[node.value] + 1
                    return
                else:
                    node = child
            elif value < node.value:
                child = node.left
                if child is None:
                    new_node = Node(value)
                    node.left = new_node
                    heights[value] = heights[node.value] + 1
                    return
                else:
                    node = child
            else:
                return


def main():
    vertices = map(int, input().split())
    root_num = next(vertices)
    root_node = Node(value=root_num)
    heights = {root_num: 1}
    for v_num in vertices:
        if v_num != 0:
            root_node.insert(v_num, heights)

    print(max(heights.values()))


if __name__ == '__main__':
    main()
