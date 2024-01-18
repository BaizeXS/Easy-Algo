"""二分查找

Question：
给定一个长度为 n 的数组 nums，元素按从小到大的顺序排列且不重复。请查找并返回
元素 target 在该数组中的索引。若数组不包含该元素，则返回 -1。

由于 i 和 j 都是 int 类型，因此 i + j 可能会超出 int 类型的取值范围，因此
通常采用公式 m = i + (j - i) / 2 来计算中点。

二分查找的复杂度
时间复杂度 O(log n)
空间复杂度 O(1)

二分查找的优点和局限性
优点
- 二分查找在时间和空间方面都有着较为良好的性能，在大数据量下有着显著的优势，并
  且无需额外的空间占用。
局限性
- 二分查找只能用于有序的数据。对于无序数据，若进行排序，得不偿失，因为排序通常
  时间复杂度为 O(n log n)，远远大于线性查找和二分查找。
- 二分查找仅适用于数组，对于链表而言效率较低。
- 小数据量下，线性查找性能更加。
"""


def binary_search(nums, target):
    """二分查找（双闭区间）"""
    # 初始化双闭区间 [0, n-1] ，即 i, j 分别指向数组首元素、尾元素
    i, j = 0, len(nums) - 1
    # 开始循环，当搜索区间为空时跳出循环
    while i <= j:
        # 理论上 Python 的数字可以无限大（取决于内存大小），无须考虑大数越界问题
        m = (i + j) // 2  # 计算中点 m
        if nums[m] < target:
            i = m + 1  # 此时说明 target 在区间 [m+1, j] 中
        elif nums[m] > target:
            j = m - 1  # 此时说明 target 在区间 [i, m-1] 中
        else:
            return m  # 找到目标元素，返回索引
    return -1  # 未找到目标元素，返回 -1


def binary_search_lcro(nums, target):
    """二分查找（左闭右开区间）"""
    i, j = 0, len(nums)
    while i < j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m
        else:
            return m
    return -1


if __name__ == '__main__':
    test_nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]
    test_target1 = 31
    test_target2 = 3
    test_target3 = 2

    print(f"Test 1: {binary_search(test_nums, test_target1)}")
    print(f"Test 2: {binary_search(test_nums, test_target2)}")
    print(f"Test 3: {binary_search(test_nums, test_target3)}")
