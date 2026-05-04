def generate_bracket_seq(n: int, s: str = "", left: int = 0, right: int = 0):
    if len(s) == 2 * n:
        print(s)
        return

    if left < n:
        generate_bracket_seq(n, s + "(", left + 1, right)
    if left > right:
        generate_bracket_seq(n, s + ")", left, right + 1)


def main():
    n = int(input())
    generate_bracket_seq(n)


if __name__ == '__main__':
    main()
