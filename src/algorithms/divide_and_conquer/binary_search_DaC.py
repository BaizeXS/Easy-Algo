def dfs(nums: list[int], target: int, i: int, j: int) -> int:
    if i > j:
        return -1
    m = (i + j) // 2
    if nums[m] < target:
        return dfs(nums, target, m + 1, j)
    elif nums[m] > target:
        return dfs(nums, target, i, m - 1)
    else:
        return m


def binary_search_DaC(nums: list[int], target: int) -> int:
    """基于分治的二分查找"""
    n = len(nums)
    return dfs(nums, target, 0, n - 1)
