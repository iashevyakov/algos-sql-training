from collections import defaultdict


def count_unique_password(s: str) -> int:
    ch_cnt = defaultdict(int)
    for ch in s:
        ch_cnt[ch] += 1
    n = len(s)
    answer = n * (n - 1) / 2
    for cnt in ch_cnt.values():
        answer -= cnt * (cnt - 1) / 2
    return answer + 1


if __name__ == "__main__":
    s = input()
    print(count_unique_password(s))
