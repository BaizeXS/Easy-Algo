"""
Max Heap implementation

1.  堆是一种特殊的完全二叉树，非常适合使用数组表示，因此我们使用数组来存储堆。
2.  使用数组表示二叉树时，元素代表节点值，索引代表节点在二叉树中的位置。
3.  节点指针通过索引映射公式实现，给定索引 i：
        - 左子节点索引： 2 * i + 1
        - 右子节点索引： 2 * i + 2
        - 父节点索引： (i - 1) // 2
    当索引越界时，表示空节点或者节点不存在。
4.  堆常见应用
    - 优先队列：堆通常作为实现优先队列的首选数据结构，其入队和出队操作的时间复杂度均为 O(log n)，
      而建队操作为 O(n)，这些操作都非常高效。
    - 堆排序：给定一组数据，我们可以用它们建立一个堆，然后不断执行元素出堆的操作，从而得到有序数据。
      然而，我们通常会使用一种更为优雅的方式实现堆排序。
    - 获取最大的 k 个元素：这是一个经典的算法问题，同时也是一种典型应用，例如选择热度前 10 的新闻
      作为微博热搜，选取销量前 10 的商品等。
"""
from __future__ import annotations

from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class MaxHeap(Generic[T]):

    def __init__(self, heap_list: list[T]):
        self.max_heap: list[T] = heap_list
        # 堆化除叶节点以外的其他所有节点
        for i in range(self.parent_index(self.size() - 1), -1, -1):
            self.sift_down(i)

    def left_index(self, index: int) -> int:
        """获取左子节点索引"""
        return 2 * index + 1

    def right_index(self, index: int) -> int:
        """获取右子节点索引"""
        return 2 * index + 2

    def parent_index(self, index: int) -> int:
        """获取父节点索引"""
        return (index - 1) // 2

    def swap(self, i: int, j: int):
        """交换元素"""
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def size(self):
        """获取堆大小"""
        return len(self.max_heap)

    def is_empty(self) -> bool:
        """判断堆是否为空"""
        return self.size() == 0

    def peek(self) -> T:
        """访问堆顶元素"""
        return self.max_heap[0]

    def push(self, value: T):
        """元素入堆"""
        # 将元素添加至堆底
        self.max_heap.append(value)
        # 从底向顶进行堆化
        self.sift_up(self.size() - 1)

    def sift_up(self, index: int):
        """从节点 index 开始，从底至顶进行堆化"""
        while True:
            parent = self.parent_index(index)
            if parent < 0 or self.max_heap[index] < self.max_heap[parent]:
                break
            self.swap(index, parent)
            index = parent

    def pop(self) -> Optional[T]:
        """元素出堆"""
        # 判空处理
        if self.is_empty():
            raise IndexError("堆为空")
        # 交换堆顶与堆底
        self.swap(0, self.size() - 1)
        # 删除节点
        value = self.max_heap[self.size() - 1]
        # 从顶到底进行堆化
        self.sift_down(0)
        # 返回堆顶元素
        return value

    def sift_down(self, index: int):
        """从节点 index 开始，从顶到底进行堆化"""
        while True:
            left, right, max_index = self.left_index(index), self.right_index(index), index
            if left < self.size() and self.max_heap[left] > self.max_heap[max_index]:
                max_index = left
            if right < self.size() and self.max_heap[right] > self.max_heap[max_index]:
                max_index = right
            # 若节点 index 最大或者索引 left / right 越界，则无需堆化，直接跳出
            if max_index == index:
                break
            self.swap(index, max_index)
            index = max_index
