"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/largest-product-two-numbers
"""


def main():
    nums = map(int, input().split())
    max_abs = 10 ** 6
    min_1, min_2 = max_abs + 1, max_abs + 1
    max_1, max_2 = -1 * max_abs - 1, -1 * max_abs - 1
    for num in nums:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2:
            max_2 = num
        if num < min_1:
            min_2 = min_1
            min_1 = num
        elif num < min_2:
            min_2 = num
    if max_1 * max_2 > min_1 * min_2:
        print(max_2, max_1)
    else:
        print(min_1, min_2)


if __name__ == '__main__':
    main()
