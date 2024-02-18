"""
Question:
给定 n 个物品，第 i 个物品的重量为 wgt[i - 1] 、价值为 val[i - 1] ，和一个容量为 cap 的背包。
每个物品只能选择一次，但可以选择物品的一部分，价值根据选择的重量比例计算，问在限定背包容量下背包中物
品的最大价值。
"""


class Item:
    """物品"""

    def __init__(self, w: int, v: int):
        self.w = w
        self.v = v


def fractional_knapsack(wgt: list[int], val: list[int], cap: int) -> int:
    """分数背包：贪心"""
    # 创建物品列表，包含两个属性：重量，价值
    items = [Item(w, v) for w, v in zip(wgt, val)]
    # 按照单位价值 item.v / item.w 从高到低进行排序
    items.sort(key=lambda item: item.v / item.w, reverse=True)
    # 循环贪心选择
    res = 0
    for item in items:
        if item.w <= cap:
            res += item.v
            cap -= item.w
        else:
            res += (item.v / item.w) * cap
            break
    return res
