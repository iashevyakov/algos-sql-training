def get_min_series_cnt(s: list[int], a: list[int]) -> int:
    events = sorted(zip(s, a))
    weight_half = sum(a) / 2
    weight_sum = 0
    for series, weight in events:
        weight_sum += weight
        if weight_sum >= weight_half:
            return series


def get_surcharge(e: int, s: list[int], a: list[int]) -> int:
    return sum(abs(e - series) * weight for series, weight in zip(s, a))


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    min_series = get_min_series_cnt(s, a)
    surcharge = get_surcharge(min_series, s, a)
    print(min_series, surcharge)
