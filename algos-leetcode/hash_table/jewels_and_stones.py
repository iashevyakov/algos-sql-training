"""
https://leetcode.com/problems/jewels-and-stones
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = {}
        for stone in stones:
            if stone in stones_dict:
                stones_dict[stone] += 1
            else:
                stones_dict[stone] = 1

        count = 0
        for jewel in jewels:
            if jewel in stones_dict:
                count += stones_dict[jewel]

        return count
