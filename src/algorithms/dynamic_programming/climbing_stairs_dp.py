def climbing_stairs_dp(n: int) -> int:
    """爬楼梯：动态规划"""
    if n == 1 or n == 2:
        return n
    # 初始化 dp 表，用于存储子问题的解
    dp = [0] * (n + 1)
    # 初始状态：预设最小子问题的解
    dp[1], dp[2] = 1, 2
    # 状态转移：从较小子问题逐步求解较大子问题
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def climbing_stairs_dp_comp(n: int) -> int:
    """爬楼梯：空间优化后的动态规划
    由于 dp[i] 仅与 dp[i - 1] 和 dp[i - 2] 有关，因此只需要这两个变量滚动前进即可。
    这种空间优化技巧被称为“滚动变量”或“滚动数组”。 
    """
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        b, a = a + b, b
    return b
