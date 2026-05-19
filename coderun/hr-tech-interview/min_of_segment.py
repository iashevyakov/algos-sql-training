"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/minimum-of-the-segment
"""

from collections import deque


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    deq = deque()

    for i in range(n):
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and nums[deq[-1]] > nums[i]:
            deq.pop()
        deq.append(i)

        if i >= k - 1:
            print(nums[deq[0]])


if __name__ == '__main__':
    main()
