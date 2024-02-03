"""
Question:
给定 n 种硬币，第 i 种硬币的面值为 coins[i—1] ，目标金额为 amt ，每种硬币可以重复选取，
问凑出目标金额的硬市组合数量。
"""


def coin_change_ii_dp(coins: list[int], amt: int) -> int:
    """零钱兑换 II ：动态规划"""
    n = len(coins)
    dp = [[0] * (amt + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(n + 1):
        for a in range(amt + 1):
            if coins[i - 1] > a:
                dp[i][a] = dp[i - 1][a]
            else:
                dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]
    return dp[n][amt]


def coin_change_dp_comp(coins: list[int], amt: int) -> int:
    """零钱兑换 II ：空间优化的动态规划"""
    n = len(coins)
    dp = [0] * (amt + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                dp[a] = dp[a]
            else:
                dp[a] = dp[a] + dp[a - coins[i - 1]]
    return dp[amt]
