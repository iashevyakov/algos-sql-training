from enum import StrEnum


class EventType(StrEnum):
    dep = "dep"
    arr = "arr"


class EventDirection(StrEnum):
    forward = "forward"
    backward = "backward"


def time_str_to_int(time_str: str) -> int:
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes


def get_bus_min_count(events: list[tuple[int, str, str]]) -> int:
    forward_bus_cnt, backward_bus_cnt = 0, 0
    min_bus_cnt = 0

    for _, event_type, event_direction in events:
        if event_type == EventType.dep:
            if event_direction is EventDirection.forward:
                if forward_bus_cnt != 0:
                    forward_bus_cnt -= 1
                else:
                    min_bus_cnt += 1
            else:
                if backward_bus_cnt != 0:
                    backward_bus_cnt -= 1
                else:
                    min_bus_cnt += 1
        else:
            if event_direction is EventDirection.forward:
                backward_bus_cnt += 1
            else:
                forward_bus_cnt += 1
    return min_bus_cnt


if __name__ == "__main__":
    events = []
    n = int(input())
    for _ in range(n):
        dep_time, arr_time = map(time_str_to_int, input().split('-'))
        events.append((dep_time, EventType.dep, EventDirection.forward))
        events.append((arr_time, EventType.arr, EventDirection.forward))
    m = int(input())
    for _ in range(m):
        dep_time, arr_time = map(time_str_to_int, input().split('-'))
        events.append((dep_time, EventType.dep, EventDirection.backward))
        events.append((arr_time, EventType.arr, EventDirection.backward))
    events.sort(key=lambda e: (e[0], e[1] == EventType.dep))
    print(get_bus_min_count(events))
