"""快速排序 Quick Sort

核心思想：

时间复杂度：O(n log n)
空间复杂度：O(n)，数组完全倒序时，达到最差递归深度 n，使用 O(n) 栈帧空间。
自适应排序：平均情况下时间复杂度为 O(n log n)，最差情况下位 O(n^2)
非稳定排序
原地排序

基准数优化
可以在数组中选取三个候选元素（通常为数组的首、中、尾元素），并将这三个候选元素的中位数作为基准数。
"""


def median_three(nums: list[int], left: int, mid: int, right: int) -> int:
    """选择三个候选元素的中位数"""
    # 使用异或运算来简化代码
    if (nums[left] < nums[mid]) ^ (nums[left] < nums[right]):
        return left
    elif (nums[mid] < nums[left]) ^ (nums[mid] < nums[right]):
        return mid
    else:
        return right


def partition(nums: list[int], left: int, right: int) -> int:
    """哨兵划分"""
    mid = median_three(nums, left, (left + right) // 2, right)
    nums[left], nums[mid] = nums[mid], nums[left]
    # 以 nums[left] 为基准数
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[left] = nums[left], nums[i]
    return i


def quick_sort(nums: list[int], left: int, right: int):
    """快速排序"""
    # 当子数组长度为 1 时终止递归
    if left >= right:
        return
    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


def quick_sort_tail_recursive(nums: list[int], left: int, right: int):
    """快速排序（尾递归优化）"""
    # 子数组长度为 1 时终止
    while left < right:
        # 哨兵划分操作
        pivot = partition(nums, left, right)
        # 对两个子数组中较短的那个执行快速排序
        if pivot - left < right - pivot:
            quick_sort_tail_recursive(nums, left, pivot - 1)
            left = pivot + 1
        else:
            quick_sort_tail_recursive(nums, pivot + 1, right)
            right = pivot - 1
