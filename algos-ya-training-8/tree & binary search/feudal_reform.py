from collections import defaultdict

n = int(input())
children = defaultdict(list)
for i in range(1, n):
    p = int(input())
    children[p].append(i)

balances = {i: b for i, b in enumerate(map(int, input().split()))}
answer = 0

for v in range(n):
    children_balances = 0
    for child in children[v]:
        children_balances += balances[child]
    cur_v_edicts = -balances[v] + children_balances
    answer += abs(cur_v_edicts)

print(answer)
