from collections import defaultdict


def get_parts_indexes(n: int, m: int, s: str, s_mixed_parts: list[str]) -> list[int]:
    s_mixed_parts_indexes = defaultdict(set)
    for i, s_part in enumerate(s_mixed_parts, start=1):
        s_mixed_parts_indexes[s_part].add(i)
    part_len, cur_idx = n // m, 0
    answer = []
    for i in range(m):
        cur_s_part = s[cur_idx: cur_idx + part_len]
        cur_idx += part_len
        answer.append(s_mixed_parts_indexes[cur_s_part].pop())
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = input()
    s_mixed_parts = [
        input() for _ in range(m)
    ]
    print(*get_parts_indexes(n, m, s, s_mixed_parts))
