"""选择排序 Selection Sort

核心思想：开启一个循环，每轮从未排序区间选择最小的元素，将其放到已排序区间的末尾。

时间复杂度： O(n^2)
空间复杂度： O(1)
非自适应排序：排序时间复杂度不受输入数据影响
非稳定排序
原地排序
"""


def selection_sort(nums: list[int]):
    n = len(nums)
    # 外循环：未排序区间为 [i, n-1]
    for i in range(n - 1):
        # 内循环：找到未排序区间内的最小元素
        k = i
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]


if __name__ == '__main__':
    num = [1, 9, 4, 5, 7, 9, 8]
    print(num)
    selection_sort(num)
    print(num)
