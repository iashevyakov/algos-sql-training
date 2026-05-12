def main():
    _ = input()
    nums = map(int, input().split())
    target = int(input())
    min_diff = 2001
    answer = None
    for num in nums:
        diff = abs(num - target)
        if diff < min_diff:
            min_diff = diff
            answer = num
    print(answer)


if __name__ == '__main__':
    main()
