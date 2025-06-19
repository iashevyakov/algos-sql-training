"""Является ли слово палиндромом."""


def is_palindrom(word: str):
    i, j = 0, len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


word = input()

print(is_palindrom(word))
