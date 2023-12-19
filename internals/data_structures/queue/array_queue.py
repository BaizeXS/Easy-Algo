from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class ArrayQueue(Generic[T]):
    """
    基于环形数组实现的队列。
    数组中删除首元素的时间复杂度为 O(n)，这会导致出队操作效率较低。我们可以采用以下巧妙方法来避免这个问题。
    我们可以使用变量 front 指向队首元素的索引，并且维护一个变量 size 用于记录队列长度。
    定义 rear = front + size，该公式计算出的 rear 指向队尾元素之后的下一个位置。
    """

    def __init__(self, capacity: int = 10):
        """初始化一个空队列"""
        if capacity <= 0:
            raise ValueError("容量必须大于0")
        self._queue: list[Optional[T]] = [None] * capacity
        self._front: int = 0
        self._size: int = 0
        self._capacity: int = capacity

    def _get_index(self, index: int) -> int:
        """计算环形队列中的实际位置"""
        return (self._front + index) % self._capacity

    def _resize(self, new_capacity: int):
        """调整队列的容量大小"""
        new_queue = [None] * new_capacity
        for i in range(self._size):
            new_queue[i] = self._queue[self._get_index(i)]
        self._queue = new_queue
        self._front = 0
        self._capacity = new_capacity

    def capacity(self) -> int:
        """获取队列容量"""
        return self._capacity

    def peek(self) -> T:
        """返回队列前端的元素，但不移除它。"""
        if self.is_empty():
            raise IndexError("队列为空，无法获取元素")
        return self._queue[self._front]

    def push(self, value: T):
        """将元素添加到队列尾部"""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # 动态扩展数组大小
        self._queue[self._get_index(self._size)] = value
        self._size += 1

    def pop(self) -> T:
        """从队列前端移除并返回元素。"""
        pop_value: T = self.peek()
        self._queue[self._front] = None  # 清除引用
        self._front = self._get_index(1)
        self._size -= 1
        if 0 < self._size <= self._capacity // 4 and self._capacity > 10:  # 缩小数组大小
            self._resize(max(self._capacity // 2, 10))
        return pop_value

    def clear(self):
        """清空队列"""
        self._front = 0
        self._size = 0

    def is_empty(self) -> bool:
        """检查队列是否为空"""
        return self._size == 0

    def size(self) -> int:
        """返回队列的元素数量"""
        return self._size

    def __iter__(self):
        """使队列可迭代"""
        for i in range(self._size):
            yield self._queue[self._get_index(i)]

    def __str__(self) -> str:
        """返回队列的字符串表示"""
        values = [str(item) for item in self]
        return f"ArrayQueue([{', '.join(values)}])"
