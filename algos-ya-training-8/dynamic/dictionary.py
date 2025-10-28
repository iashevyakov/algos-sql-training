def get_sentence_with_spaces(s: str, d: set[str]) -> str:
    s_len = len(s)
    dp = [True] + [False] * s_len
    prev = [-1] * (s_len + 1)
    for i in range(1, s_len + 1):
        for j in range(i):
            if dp[j] and s[j:i] in d:
                prev[i] = j
                dp[i] = True
                break
    i = s_len
    ans = []
    while i > 0:
        cur_prev = prev[i]
        ans.append(s[cur_prev:i])
        i = cur_prev
    return ' '.join(reversed(ans))


if __name__ == "__main__":
    s = input()
    n = int(input())
    d = set(input() for _ in range(n))
    print(get_sentence_with_spaces(s, d))
