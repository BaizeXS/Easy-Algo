"""二分查找插入点
二分查找不仅可以用于搜索目标元素，还可以用于解决许多变种问题，例如搜索目标元素的插入位置。

1.  无重复元素情况
    Question：给定一个长度为 n 的有序数组 nums 和一个元素 target，数组不存在重复元素。现将 target 插入数组 nums 中，并保持其有序性。
    若数组中已经存在元素 target，则插入到其左方。
2.  有重复元素情况
    在上一题的基础上，规定数组可能包含重复元素，其余不变。假设数组中存在多个 target ，则普通二分查找只能返回其中一个 target 的索引，而无
    法确定该元素的左边和右边还有多少 target。题目要求将目标元素插入到最左边，所以我们需要查找数组中最左一个 target 的索引。初步考虑通过下
    面方式实现：
    - 执行二分查找，得到任意一个 target 的索引，记为 k。
    - 从索引 k 开始，向左进行遍历，找到最左边的 target 时返回。
    这种方法虽然可行，但是效率极低。考虑扩展二分查找代码。
    - 当 nums[m] < target 或者 nums[m] > target 时，说明还未找到 target，因此采用普通二分查找缩小操作区间，使指针 i 和 j 向小于
      target 方向靠近。
    - 当 nums[m] == target 时，说明小于 target 的元素在区间 [i, m-1] 中，因此采用 j = m - 1 来缩小区间，使指针 j 向小于 target
      的元素靠近。
    - 循环完成后，i 指向最左边的 target，j 指向首个小于 target 的元素，因此 i 就是插入点。

"""


def binary_search_insertion_simple(nums: list[int], target: int) -> int:
    """二分查找插入点（无重复元素）"""
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            return m
    # 若未找到 target，则返回插入点 i
    return i


def binary_search_insertion(nums: list[int], target: int) -> int:
    """二分查找插入点（有重复元素）"""
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            j = m - 1
    return i
