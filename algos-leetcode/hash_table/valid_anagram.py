"""
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    ORD_A = ord('a')

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0] * 26
        count_t = [0] * 26

        for i in range(len(s)):
            count_s[ord(s[i]) - self.ORD_A] += 1
            count_t[ord(t[i]) - self.ORD_A] += 1

        return count_s == count_t
