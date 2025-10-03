"""
https://leetcode.com/problems/merge-intervals/
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        answer = []
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur_interval[1]:
                if intervals[i][1] > cur_interval[1]:
                    cur_interval = [cur_interval[0], intervals[i][1]]
            else:
                answer.append(cur_interval)
                cur_interval = intervals[i]
        answer.append(cur_interval)
        return answer
