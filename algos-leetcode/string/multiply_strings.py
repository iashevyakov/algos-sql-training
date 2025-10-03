"""
https://leetcode.com/problems/multiply-strings
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len_num_1, len_num_2 = len(num1), len(num2)

        first_num = 0
        for i in range(len_num_1):
            first_num += int(num1[i]) * 10 ** (len_num_1 - i - 1)

        second_num = 0
        for i in range(len_num_2):
            second_num += int(num2[i]) * 10 ** (len_num_2 - i - 1)

        return str(first_num * second_num)
