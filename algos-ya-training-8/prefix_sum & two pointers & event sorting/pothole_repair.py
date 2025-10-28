def get_routes_diff_arr(m: int) -> list[int]:
    routes_diff = [0] * (n + 1)
    for _ in range(m):
        left, right = map(int, input().split())
        routes_diff[left - 1] += 1
        routes_diff[right] -= 1
    return routes_diff


def get_min_routes_discomfort(routes_diff: list[int], k: int) -> int:
    section_routes = [0] * n
    cur_routes_cnt = 0
    for i in range(n):
        cur_routes_cnt += routes_diff[i]
        section_routes[i] = cur_routes_cnt

    sections = [(section_routes[i], a[i]) for i in range(n)]
    sections.sort(key=lambda x: (-x[0], -x[1]))
    routes_discomfort = sum(section_routes[i] * a[i] for i in range(n))

    i = 0
    while k > 0 and i < n:
        section_routes, potholes = sections[i]
        repair = min(k, potholes)
        routes_discomfort -= repair * section_routes
        k -= repair
        i += 1

    return routes_discomfort


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    route_diff_arr = get_routes_diff_arr(m)
    print(get_min_routes_discomfort(route_diff_arr, k))
