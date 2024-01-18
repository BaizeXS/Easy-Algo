"""归并排序 Merge Sort

核心思想：一种基于分治策略的排序算法，包含“划分”和“合并”阶段。
        1. 划分阶段：递归不断将数组从中点分开，将长数组的排序问题转换为短数组的排序问题。
        2. 合并阶段：当子数组长度为 1 时终止划分，开始合并，持续地将左右两个较短的有序数组合并为一个较长的有序数组，直至结束。

时间复杂度：O(n log n)
空间复杂度：O(n)
非自适应排序
非原地排序
稳定排序

链表排序
对于链表，归并排序相较于其他排序算法具有显著优势，可以将链表的空间复杂度优化至 O(1)
- 划分阶段：可以使用“迭代”替代“递归”来实现链表划分工作，从而省去递归使用的栈帧空间。
- 合并阶段：在链表中，节点增删操作仅需改变引用（指针）即可实现，因此合并阶段（将两个短有序链表合并为一个长有序链表）无须创建额外链表。
"""


def merge(nums: list[int], left: int, mid: int, right: int):
    """合并左子数组和右子数组"""
    # 左子区间为 [0, mid]，右子区间为 [mid + 1, right]
    # 创建临时数组 temp，用于存放合并后的结果
    temp = [0] * (right - left + 1)
    # 初始化左子数组和右子数组的起始索引
    i, j, k = left, mid + 1, 0
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            j += 1
        k += 1
    # 将左子数组和右子数组的剩余元素复制到临时数组中
    while i <= mid:
        temp[k] = nums[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = nums[j]
        j += 1
        k += 1
    # 将临时数组 tmp 中的元素复制回原数组 nums 的对应区间
    for k in range(0, len(temp)):
        nums[left + k] = temp[k]


def merge_sort(nums: list[int], left: int, right: int):
    """归并排序"""
    if left >= right:
        return
    # 划分阶段
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    # 合并阶段
    merge(nums, left, mid, right)
