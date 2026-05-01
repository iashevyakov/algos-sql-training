def check_brackets_seq(s: str) -> str | int:
    open_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i, ch in enumerate(s, start=1):
        if ch in open_brackets:
            stack.append((ch, i))
        elif ch in closing_brackets:
            if not stack or stack.pop()[0] != brackets[ch]:
                return i

    return stack[0][-1] if stack else 'Success'


if __name__ == "__main__":
    seq = input()
    print(check_brackets_seq(seq))
