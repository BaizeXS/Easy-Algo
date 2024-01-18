from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class ArrayDeque(Generic[T]):
    """基于环形数组实现的双向队列"""

    def __init__(self, capacity: int = 10):
        """初始化一个空的队列"""
        if capacity <= 0:
            raise ValueError("容量必须大于0")
        self._deque: list[Optional[T]] = [None] * capacity
        self._front: int = 0
        self._size: int = 0
        self._capacity: int = capacity

    def _get_index(self, index: int) -> int:
        """计算环形队列中的实际位置"""
        return (self._front + index) % self._capacity

    def _resize(self, new_capacity: int):
        """扩大双向队列的容量"""
        new_deque = [None] * new_capacity
        for i in range(self._size):
            new_deque[i] = self._deque[self._get_index(i)]
        self._deque = new_deque
        self._front = 0
        self._capacity = new_capacity

    def _ensure_capacity(self):
        """检查双向队列的容量"""
        if self._size == self._capacity:
            self._resize(2 * self._capacity + 1)

    def _reduce_capacity(self):
        """减小双向队列的容量"""
        if 0 < self._size <= self._capacity // 4 and self._capacity > 10:
            self._resize(max(self._capacity // 2, 10))

    def capacity(self) -> int:
        """获取双向队列容量"""
        return self._capacity

    def push_first(self, value: T):
        """在队首添加元素"""
        self._ensure_capacity()
        self._front = self._get_index(-1)
        self._deque[self._front] = value
        self._size += 1

    def push_last(self, value: T):
        """在队尾添加元素"""
        self._ensure_capacity()
        rear = self._get_index(self._size)
        self._deque[rear] = value
        self._size += 1

    def pop_first(self) -> T:
        """删除队首元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        pop_value = self._deque[self._front]
        self._front = self._get_index(1)
        self._size -= 1
        self._reduce_capacity()
        return pop_value

    def pop_last(self) -> T:
        """删除队尾元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        rear = self._get_index(self._size - 1)
        pop_value = self._deque[rear]
        self._size -= 1
        self._reduce_capacity()
        return pop_value

    def peek_first(self) -> T:
        """查看队首元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        return self._deque[self._front]

    def peek_last(self) -> T:
        """查看队尾元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        rear = self._get_index(self._size - 1)
        return self._deque[rear]

    def clear(self):
        """清空队列"""
        self._deque = [None] * self._capacity
        self._front = 0
        self._size = 0

    def is_empty(self) -> bool:
        """检查双向队列是否为空"""
        return self._size == 0

    def size(self) -> int:
        """获取双向队列长度"""
        return self._size

    def __iter__(self):
        """使双向队列可迭代"""
        for i in range(self._size):
            yield self._deque[self._get_index(i)]

    def __str__(self):
        """返回双向队列的字符串表示"""
        values = [str(value) for value in self]
        return f"ArrayDeque([{', '.join(values)}])"
