"""Является ли строка `a` исходной для строки `b`."""


def is_source_string(a: str, b: str):
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)


a, b = input().split()
print(is_source_string(a, b))
