"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/sum-of-numbers
"""


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    l, r = 0, 0
    segments_cnt, cur_sum = 0, 0
    while r < n:
        if l == r:
            if nums[l] == k:
                segments_cnt += 1
            cur_sum = nums[l]
            r += 1
        elif cur_sum + nums[r] > k:
            cur_sum -= nums[l]
            l += 1
        elif cur_sum + nums[r] < k:
            cur_sum += nums[r]
            r += 1
        else:
            cur_sum += nums[r]
            r += 1
            segments_cnt += 1
    print(segments_cnt)


if __name__ == '__main__':
    main()
