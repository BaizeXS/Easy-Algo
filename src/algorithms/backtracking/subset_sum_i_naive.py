"""Question:
给定一个正整数数组 nums 和一个目标正整数 target ，请找出所有可能的组合，使得组合中的元素和等于 target 。
给定数组无重复元素，每个元素可以被选取多次。请以列表形式返回这些组合，列表中不应包含重复组合。
"""


def backtrack(
        state: list[int], 
        target: int,
        total: int,
        choices: list[int],
        res: list[list[int]]
):
    """回溯算法：子集和 I"""
    # 子集和等于 target 时，记录解
    if total == target:
        res.append(list(state))
        return
    # 遍历所有选择
    for i in range(len(choices)):
        # 剪枝：若子集和超过 target ，则跳过该选择
        if total + choices[i] > target:
            continue
        # 尝试
        state.append(choices[i])
        # 进行下一轮
        backtrack(state, target, total + choices[i], choices, res)
        # 回退
        state.pop()


def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
    """求解子集和 I（包含重复子集）"""
    state = []
    total = 0
    res = []
    backtrack(state, target, total, nums, res)
    return res