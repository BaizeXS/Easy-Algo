"""Question: 
输入一个整数数组，数组中可能包含重复元素，返回所有不重复的排列。
"""


def backtrack(state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]):
    """回溯算法：全排列 II
    从本质上看，我们的目标是在某一轮选择中，保证多个相等的元素仅被选择一次。
    在每一轮选择中开启一个哈希表 duplicated ，用于记录该轮中已经尝试过的元素，并将重复元素剪枝：
    """
    # 当状态长度等于元素数量时，记录解
    if len(state) == len(choices):
        res.append(list(state))
        return
    # 遍历所有选择
    duplicated = set[int]()
    for i, choice in enumerate(choices):
        # 剪枝：不允许重复选择元素且不允许重复选择相等元素
        if not selected[i] and choice not in duplicated:
            # 尝试：做出选择，更新状态
            duplicated.add(choice)
            selected[i] = True
            state.append(choice)
            # 进行下一轮选择
            backtrack(state, choices, selected, res)
            # 回退：撤销选择，恢复到之前的状态
            selected[i] = False
            state.pop()


def permutations_ii(nums: list[int]) -> list[list[int]]:
    """全排列 II"""
    res = []
    backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
    return res
