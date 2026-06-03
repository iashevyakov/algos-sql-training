"""
https://coderun.yandex.ru/selections/backend-interview/problems/three-blocks-row
"""


def main():
    n = int(input())
    dp = {1: 2, 2: 4, 3: 7}
    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    print(dp[n])


if __name__ == '__main__':
    main()
