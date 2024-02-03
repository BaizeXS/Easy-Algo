"""Question:
给定一个正整数数组 nums 和一个目标正整数 target ，请找出所有可能的组合，使得组合中的元素和等于 target 。
给定数组无重复元素，每个元素可以被选取多次。请以列表形式返回这些组合，列表中不应包含重复组合。
"""


def backtrack(
        state: list[int], target: int, choices: list[int], start: int, res: list[list[int]]
):
    """回溯算法：子集和 I"""
    # 子集和等于 target 时，记录解
    if target == 0:
        res.append(list(state))
        return
    # 遍历所有选择
    # 剪枝二：从 start 开始遍历，避免产生重复子集
    for i in range(start, len(choices)):
        # 剪枝一：若子集和超过 target ，则直结束循环
        if target - choices[i] < 0:
            break
        # 尝试
        state.append(choices[i])
        # 进行下一轮
        backtrack(state, target - choices[i], choices, i, res)
        # 回退
        state.pop()


def subset_sum_i(nums: list[int], target: int) -> list[list[int]]:
    state = []
    nums.sort()
    start = 0
    res = []
    backtrack(state, target, nums, start, res)
    return res


if __name__ == "__main__":
    print(subset_sum_i([3, 4, 5], 9))
