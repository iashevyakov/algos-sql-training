"""
https://leetcode.com/problems/valid-palindrome/
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        if re.search('[\dA-z]+', s) is None:
            return True
        while i <= j:
            while not s[i].isalnum() and i < len(s) - 1:
                i += 1
            while not s[j].isalnum() and j > 0:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True