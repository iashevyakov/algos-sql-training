def get_plywood_square_side_len(a: int, b: int, s: int) -> int:
    left, right = max(a, b), max(a, b) + s
    while left < right:
        mid = (left + right + 1) // 2
        shelf_square = (mid - a) * (mid - b)
        if shelf_square > s:
            right = mid - 1
        elif shelf_square < s:
            left = mid
        else:
            return mid
    return -1


if __name__ == "__main__":
    a, b, s = map(int, input().split())
    print(get_plywood_square_side_len(a, b, s))
