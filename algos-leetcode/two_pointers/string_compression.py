"""
https://leetcode.com/problems/string-compression/
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write, length = 0, 0, len(chars)
        read_next = read + 1
        while read < length:
            while read_next < length and chars[read_next] == chars[read]:
                read_next += 1
            chars[write] = chars[read]
            write += 1
            if read_next - read > 1:
                char_cnt = read_next - read
                for d in str(char_cnt):
                    chars[write] = d
                    write += 1
            read = read_next
        return write
