"""
https://leetcode.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        pattern_dict = {}
        used_words = set()
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                if words[i] in used_words:
                    return False
                pattern_dict[pattern[i]] = words[i]
                used_words.add(words[i])
            else:
                if pattern_dict[pattern[i]] != words[i]:
                    return False
        return True
