def for_loop(n: int) -> int:
    """for 循环"""
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


def while_loop(n: int) -> int:
    """while 循环"""
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res


def while_loop_ii(n: int) -> int:
    """while 循环（两次更新）"""
    res = 0
    i = 1  # 初始化条件变量
    # 循环求和 1, 4, 10, ...
    while i <= n:
        res += i
        # 更新条件变量
        i += 1
        i *= 2
    return res


def nested_for_loop(n: int) -> int:
    """双层 for 循环"""
    res = ""
    # 循环 i = 1, 2, 3, ..., n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"({i}, {j}), "
    return res


if __name__ == "__main__":
    print("for loop: ", for_loop(10))
    print("while loop: ", while_loop(10))
    print("while loop twice: ", while_loop_ii(10))
    print("nested for loop: ", nested_for_loop(10))
