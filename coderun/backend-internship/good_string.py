import sys


def main():
    n = int(input())
    counts = [int(input()) for _ in range(n)]
    answer = 0
    for i in range(1, n):
        answer += min(counts[i - 1], counts[i])
    print(answer)


if __name__ == '__main__':
    main()
