def check(k: float, w: int, h: int, words: list[tuple[int, ...]]) -> bool:
    w_sum, h_sum = words[0][0] * k, words[0][1] * k
    if w_sum > w or h_sum > h:
        return False

    i = 1
    while i < len(words):
        word = words[i]
        a_k = word[0] * k
        b_k = word[1] * k
        if a_k > w or b_k > h:
            return False
        if word[1] == words[i - 1][1] and a_k + w_sum <= w:
            w_sum += a_k
        else:
            w_sum = a_k
            h_sum += b_k

        if h_sum > h:
            return False
        i += 1

    return True


def get_max_word_scale(w: int, h: int, words: list[tuple[int, ...]]) -> int:
    left, right = 0, max(w, h)
    eps = 1e-7
    while left + eps < right:
        mid = (left + right) / 2
        if check(mid, w, h, words):
            left = mid
        else:
            right = mid
    return left


if __name__ == "__main__":
    n, w, h = map(int, input().split())
    words = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    print(get_max_word_scale(w, h, words))
