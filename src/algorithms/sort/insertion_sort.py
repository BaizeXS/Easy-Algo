"""插入排序 Insertion Sort

核心思想：在未排序区间选择一个基准元素，将该元素与其左侧已排序区间的元素逐一比较大小，并将该元素插入到正确的位置。

时间复杂度：O(n^2)
空间复杂度：O(1)
自适应排序：当输入数组完全有序时，插入排序达到最佳时间复杂度 O(n)
稳定排序
原地排序

插入排序的优势：
插入排序的时间复杂度为 O(n^2)，但是在数据量较小的情况下，插入排序通常更快。相比于时间复杂度同样为 O(n^2) 的排序
方法，插入排序有以下优势：
- 稳定排序，可以用于多级排序，而原则排序是不稳定的。
- 选择排序在任何情况下的时间复杂度都是 O(n^2)，如果数组部分有序，插入排序往往更快。
- 冒泡排序基于元素交换实现，计算开销要大于插入排序。
"""


def insertion_sort(nums: list[int]):
    n = len(nums)
    for i in range(1, n):
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = base


if __name__ == '__main__':
    num = [1, 9, 4, 5, 7, 9, 8]
    print(num)
    insertion_sort(num)
    print(num)
