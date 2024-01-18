"""堆排序 Heap Sort

核心思想：
1. 输入数组并建立大顶堆。完成后，最大元素位于堆顶。
2. 将堆顶元素与堆底元素交换。完成交换后，堆的长度减 1，已排序元素数量加 1。
3. 从堆顶元素开始，从顶到底执行堆化操作（Sift Down）。完成堆化后，堆的性质得到修复。
4. 循环执行第 2 步和第 3 步。循环 n - 1 轮后，即可完成数组排序。

时间复杂度：O(n log n)
空间复杂度：O(1)
非自适应排序
原地排序
非稳定排序
"""


def sift_down(nums: list[int], valid_length: int, index: int):
    """堆的长度为 n，从节点 index 开始从顶至底堆化"""
    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        max_index = index
        if left < valid_length and nums[left] > nums[max_index]:
            max_index = left
        if right < valid_length and nums[right] > nums[max_index]:
            max_index = right
        if max_index == index:
            break
        # 交换两个节点
        nums[max_index], nums[index] = nums[index], nums[max_index]
        # 循环向下堆化
        index = max_index


def heap_sort(nums: list[int]):
    """堆排序"""
    # 建堆操作：从最后一个非叶子节点开始进行堆化操作
    n = len(nums)
    for index in range(n // 2 - 1, -1, -1):
        sift_down(nums, n, index)
    # 排序操作：从堆中提取最大元素，循环 n - 1 轮
    for i in range(n - 1, 0, -1):
        # 交换根节点和最右叶子节点
        nums[0], nums[i] = nums[i], nums[0]
        # 从顶至底进行堆化操作
        sift_down(nums, i, 0)
