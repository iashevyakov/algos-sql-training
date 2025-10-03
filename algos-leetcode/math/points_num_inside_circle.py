"""
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle
"""
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for query in queries:
            c = 0
            for point in points:
                if (point[0] - query[0]) ** 2 + (point[1] - query[1]) ** 2 <= query[2] ** 2:
                    c += 1
            answer.append(c)
        return answer
