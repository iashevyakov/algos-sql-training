from typing import List


class Solution:
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        min_len_str = next(filter(lambda s: len(s) == min_len, strs))
        prefix = ""
        for idx, char in enumerate(min_len_str):
            for s in strs:
                if s[idx] != char:
                    return prefix
            prefix += char
        return prefix
