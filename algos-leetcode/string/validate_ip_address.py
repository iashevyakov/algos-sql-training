"""
https://leetcode.com/problems/validate-ip-address
"""
import re


class Solution:
    NEITHER = "Neither"
    IP_V4 = "IPv4"
    IP_V6 = "IPv6"
    HEXDIGITS = "0123456789abcdefABCDEF"

    def valid_ip_v4(self, parts: list[str]) -> str:
        for part in parts:
            if part != '0' and part.startswith('0'):
                return self.NEITHER
            try:
                part_int = int(part)
            except ValueError:
                return self.NEITHER
            if not 0 <= part_int <= 255:
                return self.NEITHER
        return self.IP_V4

    def valid_ip_v6(self, parts: list[str]) -> str:
        for part in parts:
            if re.match('^[\dabcdefABCDEF]{1,4}$', part) is None:
                return self.NEITHER
        return self.IP_V6

    def validIPAddress(self, queryIP: str) -> str:
        parts = queryIP.split('.')
        if len(parts) == 4:
            return self.valid_ip_v4(parts)
        elif len(parts) == 1:
            parts = queryIP.split(':')
            if len(parts) == 8:
                return self.valid_ip_v6(parts)
            return self.NEITHER
        return self.NEITHER
