"""
https://coderun.yandex.ru/selections/yandex-interview/problems/consecutive-ones/description
"""


def main() -> int:
    n = int(input())
    nums = map(int, (input() for _ in range(n)))
    max_ones_seq_len = 0
    left, right = -1, -1
    for i, num in enumerate(nums):
        if num == 1:
            if left == -1:
                left, right = i, i
            else:
                right = i
            ones_seq_len = right - left + 1
            max_ones_seq_len = max(max_ones_seq_len, ones_seq_len)
        else:
            left = -1
    return max_ones_seq_len


if __name__ == '__main__':
    answer = main()
    print(answer)
