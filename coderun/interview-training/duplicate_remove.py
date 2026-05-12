"""
https://coderun.yandex.ru/selections/yandex-interview/problems/removing-duplicates
"""

def main():
    n = int(input())
    last_unique_num = None
    for _ in range(n):
        num = int(input())
        if num != last_unique_num:
            print(num)
            last_unique_num = num


if __name__ == '__main__':
    main()
