def get_k_topics(n: int, k: int, topics: list[int]) -> list[int]:
    unique_topics = set()
    answer = []
    for i, t in enumerate(topics):
        answer_len = len(answer)
        if len(answer) == k:
            break
        if n - 1 - i < k - answer_len:
            answer.append(t)
        elif t not in unique_topics:
            answer.append(t)
            unique_topics.add(t)
    return answer


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(*get_k_topics(n, k, a))
