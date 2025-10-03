"""
https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        min_len_str = next(filter(lambda s: len(s) == min_len, strs))
        prefix = ""
        for idx, char in enumerate(min_len_str):
            for s in strs:
                if s[idx] != char:
                    return prefix
            prefix += char
        return prefix
