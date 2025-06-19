"""Является ли слово палиндромом."""


def is_palindrom(word: str):
    word_stack = []
    for char in word:
        word_stack.append(char)

    for char in word:
        if char != word_stack.pop():
            return False
    return True


word = input()

print(is_palindrom(word))
