"""二分查找边界

查找左边界
Question：给定一个长度为 n 的有序数组 nums，其中可能包含重复元素。请返回数组中最左一个元素 target 的索引。
若数组中不包含该元素，则返回 -1。

回忆二分查找插入点的方法，搜索完成后 i 指向最左的一个 target，因此查找插入点本质上是在查找最左一个 target 的
缩影，考虑通过查找插入点的函数实现查找左边界。若数组中不包含 target，则有以下两种可能：
- 插入点的索引 i 越界
- 元素 nums[i] 与 target 不相等


查找右边界
最直接的方法是修改代码，替换 nums[m] == target 情况下的指针收缩操作。下面介绍两种更为取巧的方法。
1.  复用查找左边界
    实际上，我们可以利用查找最左元素的函数来查找最右元素，具体方法为：将查找最右一个 target 转化为查找最左一个
    target + 1。
2.  转化为查找元素
    当数组不包含 target 时，最终 i 和 j 会分别指向首个大于、小于 target 的元素。因此，我们可以构造一个不存
    在的元素用于查找左右边界。
    - 查找最左一个 target：可以转化成查找 target - 0.5，并返回指针 i
    - 查找最右一个 target：可以转化成查找 target + 0.5，并返回指针 j
"""
from src.algorithms.search.binary_search_insertion import binary_search_insertion


def binary_search_left_edge(nums, target):
    index = binary_search_insertion(nums, target)
    if index == len(nums) or target != nums[index]:
        return -1
    return index


def binary_search_right_edge(nums: list[int], target: int) -> int:
    """二分查找最右一个 target"""
    i = binary_search_insertion(nums, target + 1)
    # j 指向最右一个 target ，i 指向首个大于 target 的元素
    j = i - 1
    # 未找到 target ，返回 -1
    if j == -1 or nums[j] != target:
        return -1
    # 找到 target ，返回索引 j
    return j
