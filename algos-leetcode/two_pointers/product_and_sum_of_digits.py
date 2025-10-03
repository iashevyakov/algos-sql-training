"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_, product = 0, 1
        while n != 0:
            digit = n % 10
            sum_ += digit
            product *= digit
            n //= 10
        return product - sum_
