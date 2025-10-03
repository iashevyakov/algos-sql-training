"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import Optional, List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write, length = 0, 0, len(nums)
        read_next = read + 1
        while read < length:
            while read_next < length and nums[read_next] == nums[read]:
                read_next += 1
            write += 1
            if read_next < length:
                nums[write] = nums[read_next]
            read = read_next
        return write
