"""
https://coderun.yandex.ru/selections/hr-tech-interview/problems/correct-bracket-sequence
"""
from collections import deque


def main() -> bool:
    stack = deque()
    brackets = {')': '(', ']': '[', '}': '{'}
    open_brackets = {'(', '[', '{'}
    s = input()
    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif not stack or brackets[char] != stack.pop():
            return False
    return not stack


if __name__ == '__main__':
    is_seq_correct = main()
    print("yes" if is_seq_correct else "no")
