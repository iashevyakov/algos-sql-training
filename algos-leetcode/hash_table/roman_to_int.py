"""
https://leetcode.com/problems/roman-to-integer/
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(s)):
            ch_int = roman_to_int[s[i]]
            if i + 1 < len(s) and ch_int < roman_to_int[s[i + 1]]:
                result -= ch_int
            else:
                result += ch_int
        return result