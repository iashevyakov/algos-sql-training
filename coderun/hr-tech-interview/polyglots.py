"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/polyglots
"""

from collections import defaultdict

def main():
    n = int(input())
    lang_freq = defaultdict(int)
    popular_langs = []
    for _ in range(n):
        m = int(input())
        for __ in range(m):
            lang = input()
            lang_freq[lang] += 1
            if lang_freq[lang] == n:
                popular_langs.append(lang)
    print(len(popular_langs))
    for lang in popular_langs:
        print(lang)
    print(len(lang_freq))
    for lang in lang_freq.keys():
        print(lang)



if __name__ == '__main__':
    main()