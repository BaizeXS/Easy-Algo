def dfs(i: int) -> int:
    """搜索"""
    if i == 1 or i == 2:
        return i
    count = dfs(i - 1) + dfs(i - 2)
    return count


def climbing_stairs_dfs(n: int) -> int:
    """爬楼梯：搜索"""
    return dfs(n)


if __name__ == "__main__":
    print(climbing_stairs_dfs(6))
