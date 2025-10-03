"""
https://leetcode.com/problems/merge-strings-alternately
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1, len_2 = len(word1), len(word2)
        min_len = min(len_1, len_2)
        answer = ''
        for i in range(min_len):
            answer += word1[i] + word2[i]
        for j in range(min_len, len_1):
            answer += word1[j]
        for k in range(min_len, len_2):
            answer += word2[k]
        return answer
