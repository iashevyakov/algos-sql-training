def min_buy_time(a: int, b: int, c: int, v0: int, v1: int, v2: int):
    case_1 = a / v0 + a / v1 + b / v0 + b / v1

    case_sm_first_1 = a / v0 + c / v1 + b / v2
    case_sm_first_2 = a / v0 + c / v0 + c / v1 + a / v2
    case_sm_first_3 = a / v0 + c / v1 + c / v2 + a / v2
    case_sm_first_4 = a / v0 + a / v1 + (a + c) / v0 + (a + c) / v1

    case_pp_first_1 = b / v0 + c / v1 + a / v2
    case_pp_first_2 = b / v0 + c / v0 + c / v1 + b / v2
    case_pp_first_3 = b / v0 + c / v1 + c / v2 + b / v2
    case_pp_first_4 = b / v0 + b / v1 + (b + c) / v0 + (b + c) / v1

    return min(
        case_1,
        case_sm_first_1, case_sm_first_2, case_sm_first_3, case_sm_first_4,
        case_pp_first_1, case_pp_first_2, case_pp_first_3, case_pp_first_4
    )


if __name__ == "__main__":
    a, b, c, v0, v1, v2 = map(int, input().split())
    print(min_buy_time(a, b, c, v0, v1, v2))
