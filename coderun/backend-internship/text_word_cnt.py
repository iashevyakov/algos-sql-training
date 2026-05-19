"""
https://coderun.yandex.ru/selections/backend-interview/problems/number-words-text
"""

import sys


def main():
    text = sys.stdin.read()
    unique_words = set(text.split())
    print(len(unique_words))


if __name__ == '__main__':
    main()
