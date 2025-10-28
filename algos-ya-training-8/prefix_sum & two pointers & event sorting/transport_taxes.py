from bisect import bisect_left


def get_power_tax(powers: list[int], tax_rates: list[int], power: int) -> int:
    pos = bisect_left(powers, power)
    tax_rate = tax_rates[pos - 1]
    return tax_rate * power


if __name__ == '__main__':
    n = int(input())
    powers, tax_rates = [], []
    for _ in range(n):
        power, tax = map(int, input().split())
        powers.append(power)
        tax_rates.append(tax)

    m = int(input())
    for _ in range(m):
        power = int(input())
        print(get_power_tax(powers, tax_rates, power))
