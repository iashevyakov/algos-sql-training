from collections import defaultdict


def main():
    s1, s2 = input(), input()
    if len(s1) != len(s2):
        return 0
    s1_counter = defaultdict(int)
    for ch1 in s1:
        s1_counter[ch1] += 1
    for ch2 in s2:
        if not s1_counter.get(ch2):
            return 0
        s1_counter[ch2] -= 1
    return 1



if __name__ == '__main__':
    answer = main()
    print(answer)