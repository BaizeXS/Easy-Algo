"""冒泡排序 Bubble Sort

核心思想：通过连续地比较与交换相邻元素实现排序。

时间复杂度：O(n^2)
空间复杂度：O(1)
自适应排序：引入 flag 优化后，最佳时间复杂度可的达到 O(n)
稳定排序
原地排序
"""


def bubble_sort(nums: list[int]):
    n = len(nums)
    # 外循环：未排序区间为 [0, i]
    for i in range(n - 1, 0, -1):
        # 内循环：将未排序区间 [0, i] 中的最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def bubble_sort_with_flag(nums: list[int]):
    """冒泡排序（标志优化）"""
    n = len(nums)
    for i in range(n - 1, 0, -1):
        flag = False
        for j in range(i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
            if not flag:
                break


if __name__ == '__main__':
    num = [2, 4, 5, 1, 3, 6, 1, 2]
    print(num)
    bubble_sort(num)
    print(num)
