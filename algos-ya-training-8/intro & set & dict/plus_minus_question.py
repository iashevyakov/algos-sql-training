from collections import defaultdict


def get_max_diff(n: int, m: int, table: list[list[str]]) -> int:
    cnt_row_dict = defaultdict(int)
    cnt_column_dict = defaultdict(int)
    answer = float('-inf')
    for i, row in enumerate(table):
        for j, ch in enumerate(row):
            if ch == '+':
                cnt_row_dict[i] += 1
                cnt_column_dict[j] += 1
            elif ch == '-':
                cnt_row_dict[i] -= 1
                cnt_column_dict[j] -= 1
            else:
                cnt_row_dict[i] += 1
                cnt_column_dict[j] -= 1
    for i in range(n):
        row_value = cnt_row_dict[i]
        for j in range(m):
            col_value = cnt_column_dict[j]
            row_col_diff = row_value - col_value
            if table[i][j] == '?':
                row_col_diff -= 2
            if row_col_diff > answer:
                answer = row_col_diff
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(input()))
    print(get_max_diff(n, m, table))
