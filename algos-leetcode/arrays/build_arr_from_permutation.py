"""
https://leetcode.com/problems/build-array-from-permutation
"""
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]
