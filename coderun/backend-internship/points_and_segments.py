"""
https://coderun.yandex.ru/selections/backend-interview/problems/points-and-segments
"""

def main():
    n, m = map(int, input().split())
    events = []
    for _ in range(n):
        p1, p2 = map(int, input().split())
        l, r = min(p1, p2), max(p1, p2)
        events.append([l, -1, 0])
        events.append([r, 1, 0])
    points = map(int, input().split())
    for i, p in enumerate(points):
        events.append([p, 0, i])
    events.sort(key=lambda x: (x[0], x[1]))

    answer, active_segments = [0] * m, 0
    for point, event_type, idx in events:
        if event_type == -1:
            active_segments += 1
        elif event_type == 1:
            active_segments -= 1
        else:
            answer[idx] = active_segments

    print(*answer)


if __name__ == '__main__':
    main()
