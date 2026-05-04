"""
https://coderun.yandex.ru/selections/yandex-interview/problems/rocks-and-jewels
"""


def main():
    j, s = input(), input()
    j_chars = set(j)
    answer = 0
    for ch in s:
        if ch in j_chars:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
