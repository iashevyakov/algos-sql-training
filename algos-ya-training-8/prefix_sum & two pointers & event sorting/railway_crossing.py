from bisect import bisect_right
from collections import defaultdict


def get_active_trains_after_times(times: list[float], times_counter: dict):
    active_trains_after_times = [0] * len(times)
    curr_train_cnt = 0
    for i, time in enumerate(times):
        curr_train_cnt += times_counter[time]
        active_trains_after_times[i] = curr_train_cnt
    return active_trains_after_times


def get_release_times(
    active_trains_after_times: list[int], times: list[float], times_counter: dict
) -> list[float]:
    release_times = []
    for i in range(len(times)):
        time = times[i]
        after_trains = active_trains_after_times[i]
        before_trains = active_trains_after_times[i] - times_counter[time]
        if before_trains > 0 > times_counter[time] and after_trains == 0:
            release_times.append(time)
    return release_times


def print_destination_car_times(car_times: list[int], times: list[float], release_times: list[float]):
    for car_time in car_times:
        idx = bisect_right(times, car_time)
        trains_after_car_time = trains_after_times[idx - 1] if idx > 0 else 0
        if trains_after_car_time:
            max_release_idx = bisect_right(release_times, car_time)
            print(release_times[max_release_idx])
        else:
            print(car_time)


if __name__ == "__main__":
    n, m, x = map(int, input().split())
    time_counter = defaultdict(int)
    for _ in range(n):
        a, b, v = map(int, input().split())
        if a < b:
            train_start, train_end = (x - b) / v, (x - a) / v
        else:
            train_start, train_end = (b - x) / v, (a - x) / v
        if train_end >= 0 and train_start <= train_end:
            train_start = max(0, train_start)
            time_counter[train_start] += 1
            time_counter[train_end] -= 1

    car_times = list(map(int, input().split()))
    times = sorted(time_counter.keys())
    trains_after_times = get_active_trains_after_times(times, time_counter)

    release_times = get_release_times(trains_after_times, times, time_counter)
    print_destination_car_times(car_times, times, release_times)
