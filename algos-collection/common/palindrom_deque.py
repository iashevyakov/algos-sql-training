"""Является ли слово палиндромом."""
from collections import deque


def is_palindrom(word: str):
    word_deque = deque()
    for char in word:
        word_deque.append(char)

    while len(word_deque) > 1:
        if word_deque.popleft() != word_deque.pop():
            return False
    return True


word = input()

print(is_palindrom(word))
