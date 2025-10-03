"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        unique_chars = set()
        answer = 0
        while left <= right and right < len(s):
            if s[right] not in unique_chars:
                unique_chars.add(s[right])
                right += 1
                answer = max(answer, right - left)
            else:
                while s[right] in unique_chars:
                    unique_chars.remove(s[left])
                    left += 1
        return answer
