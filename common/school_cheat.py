n = int(input())
scores = input().split()

ZERO_CHAR = '0'
zeros_cnt = 0

for s in scores:
    if s == ZERO_CHAR:
        zeros_cnt += 1
    else:
        print(s, end=' ')

print(' '.join(ZERO_CHAR for _ in range(zeros_cnt)))
