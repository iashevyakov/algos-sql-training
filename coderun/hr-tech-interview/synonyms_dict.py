"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/dictionary-synonyms
"""


def main():
    n = int(input())
    synonyms = {}
    for _ in range(n):
        word_1, word_2 = input().split(" ")
        synonyms[word_1] = word_2
        synonyms[word_2] = word_1
    word = input()
    print(synonyms[word])


if __name__ == '__main__':
    main()
