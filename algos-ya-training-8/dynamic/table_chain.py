import sys
sys.setrecursionlimit(100000000000000)

def get_chain_length(i: int, j: int, chain_lengths: dict, table: list[list[int]], n: int, m: int) -> int:
    if (i, j) in chain_lengths:
        return chain_lengths[(i, j)]

    table_num = table[i][j]
    max_chain_len = 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for di, dj in directions:
        ii, jj = i + di, j + dj
        if 0 <= ii < n and 0 <= jj < m:
            neighbor_num = table[ii][jj]
            if neighbor_num == table_num + 1:
                chain_len = 1 + get_chain_length(ii, jj, chain_lengths, table, n, m)
                max_chain_len = max(max_chain_len, chain_len)
    chain_lengths[(i, j)] = max_chain_len
    return max_chain_len


def get_max_chain_length(n: int, m: int, table: list[list[int]]) -> int:
    max_chain_length = 0
    chain_lengths = {}
    for i in range(n):
        for j in range(m):
            chain_length = get_chain_length(i, j, chain_lengths, table, n, m)
            max_chain_length = max(max_chain_length, chain_length)
    return max_chain_length


if __name__ == "__main__":
    n, m = map(int, input().split())
    table = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    print(get_max_chain_length(n, m, table))