"""
https://leetcode.com/problems/plus-one
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur_i = len(digits) - 1
        while cur_i >= 0 and digits[cur_i] == 9:
            digits[cur_i] = 0
            cur_i -= 1
        if cur_i == -1:
            digits.insert(0, 1)
        else:
            digits[cur_i] += 1
        return digits
