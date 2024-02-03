"""Question:
给定一个正整数数组 nums 和一个目标正整数 target ，请找出所有可能的组合，使得组合中的元素和等于 target 。
给定数组可能包含重复元素，每个元素只可被选择一次。请以列表形式返回这些组合，列表中不应包含重复组合。
"""


def backtrack(state: list[int], target: int, choices: list[int], start: int, res: list[list[int]]):
    """回溯算法：子集和 II"""
    # 子集和等于 target 时，记录解
    if target == 0:
        res.append(list(state))
        return
    # 遍历所有选择
    # 剪枝二：从 start 开始遍历，避免生成重复子集
    # 剪枝三：从 start 开始遍历，避免重复选择同一元素
    for i in range(start, len(choices)):
        # 剪枝一：若子集和超过 target ，则直接结束循环（因为已排序）
        if target - choices[i] < 0:
            break
        # 剪枝四：如果该元素与左边元素相等，则说明该搜索分支重复，直接跳过
        if i > start and choices[i] > choices[i - 1]:
            continue
        # 尝试
        state.append(choices[i])
        # 下一轮
        backtrack(state, target - choices[i], choices, i + 1, res)
        # 回退
        state.pop()


def subset_sum_ii(nums: list[int], target: int):
    """求解子集和 II"""
    state = []
    nums.sort()
    start = 0
    res = []
    backtrack(state, target, nums, start, res)
    return res


if __name__ == "__main__":
    nums = [4, 4, 5]
    target = 9
    print(subset_sum_ii(nums, target))
