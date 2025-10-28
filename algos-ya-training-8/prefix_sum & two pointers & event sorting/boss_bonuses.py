def get_boss_bonuses(n: int, a: list[int]) -> int:
    diff = [0] * (n + 2)
    for j in range(n):
        left, right = j + 1, j + a[j]
        if left < n:
            diff[left] += 1
        if right < n:
            diff[right] -= 1
    bonuses_answer, bonuses_sum = 0, 0
    for i in range(n):
        bonuses_sum += diff[i]
        bonuses_answer += a[i] * bonuses_sum
    return bonuses_answer


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_boss_bonuses(n, a))
