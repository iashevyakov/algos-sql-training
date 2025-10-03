"""
https://leetcode.com/problems/find-the-distance-value-between-two-arrays
"""

from bisect import bisect_left
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        answer = 0
        for e1 in arr1:
            idx = bisect_left(arr2, e1)
            if idx < len(arr2) and arr2[idx] - e1 <= d:
                continue
            if idx > 0 and e1 - arr2[idx - 1] <= d:
                continue
            answer += 1
        return answer
