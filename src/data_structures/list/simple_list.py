from typing import Iterable


class SimpleList:
    """列表类"""

    def __init__(self):
        self._capacity: int = 10  # 初始容量
        self._extend_ratio: int = 2  # 扩容倍数
        self._size: int = 0  # 当前元素数量
        self._data: list = [None] * self._capacity  # 内部数组

    @property
    def capacity(self) -> int:
        """获取列表容量"""
        return self._capacity

    def _check_index(self, index: int, for_insert: bool = False) -> None:
        if for_insert and index > self._size:
            raise IndexError(f"索引越界: {index}")
        elif not for_insert and (index < 0 or index >= self._size):
            raise IndexError(f"索引越界: {index}")

    def _resize(self, new_capacity: int = None) -> None:
        """
        扩容机制（理论）：
        new_capacity = self._capacity * self._extend_radio  # 获取新的列表容量
        new_data = [None] * new_capacity  # 根据新的列表容量建立新的列表
        for i in range(self._size):  # 复制原数组的内容到新数组
            new_data[i] = self._data[i]
        self._data = new_data  # 更改列表数组指向
        """
        if new_capacity is None:
            new_capacity = self._capacity * self._extend_ratio
        self._data += [None] * (new_capacity - self._capacity)
        self._capacity = new_capacity

    def append(self, item) -> None:
        if self._size == self._capacity:
            self._resize()
        self._data[self._size] = item
        self._size += 1

    def insert(self, index: int, item) -> None:
        """
        在 index 处插入元素（理论）：

        """
        self._check_index(index, True)
        if self._size == self._capacity:
            self._resize()
        self._data[index + 1:self._size + 1] = self._data[index:self._size]
        self._data[index] = item
        self._size += 1

    def remove(self, index: int) -> None:
        """
        移除 index 处的元素（理论）：
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        """
        self._check_index(index)
        self._data[index:self._size - 1] = self._data[index + 1:self._size]
        self._data[self._size - 1] = None
        self._size -= 1

    def extend(self, iterable: Iterable) -> None:
        """
        添加可迭代对象至列表（理论）：
        for item in iterable:
            self.append(item)
        """
        items = list(iterable)
        new_size = self._size + len(items)
        if new_size > self._capacity:
            self._resize(new_size)
        self._data[self._size:new_size] = items
        self._size += new_size

    def clear(self) -> None:
        self._size = 0

    def count(self, item) -> int:
        return sum(1 for elem in self._data[:self._size] if elem == item)

    def __getitem__(self, index: int):
        self._check_index(index)
        return self._data[index]

    def __setitem__(self, index: int, value) -> None:
        self._check_index(index)
        self._data[index] = value

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return str(self._data[:self._size])

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]
