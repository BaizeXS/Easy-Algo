"""
Question:
给定 n 种硬币，第 i 种硬币的面值为 coins[i - 1] ，目标金额为 amt ，每种硬币可以重复选取，
问能够凑出目标金额的最少硬币数量。如果无法凑出目标金额，则返回 -1 。
"""


def coin_change_greedy(coins: list[int], amt: int) -> int:
    """零钱兑换：贪心"""
    # 假设 coins 列表有序
    # coins.sort()
    i = len(coins) - 1
    count = 0
    # 循环进行贪心选择，直到无剩余金额
    while amt > 0:
        # 找到小于且最接近剩余金额的硬币
        while i > 0 and coins[i] > amt:
            i -= 1
        # 选择 coins[i]
        amt -= coins[i]
        count += 1
    # 若未能找到可行方案，则返回 -1
    return count if amt == 0 else -1


if __name__ == "__main__":
    coins = [186, 419, 83, 408]
    amt = 6249
    print(coin_change_greedy(coins, amt))
