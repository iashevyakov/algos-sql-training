def max_mushroom_diff(n: int, weights: list[int]) -> int:
    weights_1_sum = sum(weights[i] for i in range(0, n, 2))
    weights_1_min = min(weights[i] for i in range(0, n, 2))

    weights_2_sum = sum(weights[i] for i in range(1, n, 2))
    weights_2_max = max(weights[i] for i in range(1, n, 2))
    return weights_1_sum - weights_2_sum + 2 * max(weights_2_max - weights_1_min, 0)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(max_mushroom_diff(n, a))
