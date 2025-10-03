"""
https://leetcode.com/problems/valid-mountain-array
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        left_v, right_v = False, False
        left, right = 0, n - 1
        while left + 1 < right:
            if arr[left] >= arr[left + 1]:
                left_v = True
            elif arr[left] == arr[left + 1]:
                return False
            else:
                left += 1

            if arr[right - 1] < arr[right]:
                right_v = True
            elif arr[right - 1] == arr[right]:
                return False
            else:
                right -= 1
            if left_v and right_v:
                return False
        return left != 0 and right != n - 1
