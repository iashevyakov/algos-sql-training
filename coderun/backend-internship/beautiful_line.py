"""
https://coderun.yandex.ru/selections/backend-interview/problems/beautiful-line
"""


def main():
    k = int(input())
    s = input()
    unique_chars = set(s)
    max_beauty = 0
    for char in unique_chars:
        l, replacements = 0, 0
        for r in range(0, len(s)):
            if s[r] != char:
                replacements += 1
            while replacements > k:
                if s[l] != char:
                    replacements -= 1
                l += 1
            max_beauty = max(max_beauty, r - l + 1)
    print(max_beauty)



if __name__ == '__main__':
    main()
