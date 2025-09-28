from collections import defaultdict


def main_element(n: int, nums: list[int]) -> int:
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
        if counts[num] > n / 2:
            return num
    return -1


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(main_element(n, nums))
