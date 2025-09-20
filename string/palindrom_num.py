# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if x_str[0] == '-':
            return False
        i, j = 0, len(x_str) - 1
        while i < j:
            if x_str[i] != x_str[j]:
                return False
            i += 1
            j -= 1
        return True
