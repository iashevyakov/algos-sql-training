def get_last_check_container(n: int, nums: list[int]):
    for i in range(n - 1, -1, -1):
        if nums[i] % 2 == 0:
            return nums[i]
    return -1


n = int(input())

containers_nums = list(map(int, input().split()))

print(get_last_check_container(n, containers_nums))
