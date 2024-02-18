"""
链表
"""

from __future__ import annotations
from typing import TypeVar, Generic, Optional, Iterator
from components import ListNode


T = TypeVar("T")


class LinkedList(Generic[T]):
    """单向链表类"""

    def __init__(self):
        self.head: Optional[ListNode[T]] = None
        self.tail: Optional[ListNode[T]] = None
        self._size: int = 0

    def append(self, value: T):
        """在链表尾部添加一个新元素"""
        node = ListNode(value)
        if self.head is None:
            self.head = node
        else:
            assert self.tail is not None  # 为了类型检查
            self.tail.next = node
        self.tail = node
        self._size += 1

    def prepend(self, value: T):
        """在链表头部添加一个新元素"""
        self.head = ListNode(value, self.head)
        if self.tail is None:
            self.tail = self.head
        self._size += 1

    def insert(self, index: int, value: T):
        """在索引 index 处插入元素"""
        if index == 0:
            self.prepend(value)
            return
        elif index == self._size:
            self.append(value)
            return

        previous = self._get_node(index - 1)
        previous.next = ListNode(value, previous.next)
        self._size += 1

    def _get_node(self, index: int) -> ListNode[T]:
        """获取指定索引的节点"""
        if index < 0 or index >= self._size:
            raise IndexError(f"索引越界: {index}")

        current = self.head
        for _ in range(index):
            assert current is not None
            current = current.next
        return current

    def delete(self, value: T):
        """删除链表中第一个值为 value 的节点"""
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if previous is None:  # 删除的是头节点
                    self.head = self.head.next
                    if self.head is None:  # 删除头节点后链表为空
                        self.tail = None
                else:  # 删除的是中间节点或尾节点
                    previous.next = current.next
                    if current.next is None:  # 删除的是尾节点
                        self.tail = previous
                self._size -= 1
                return
            previous = current
            current = current.next

    def delete_at(self, index: int):
        """删除链表中索引为 index 的节点"""
        if index < 0 or index >= self._size:
            raise IndexError(f"索引越界: {index}")

        if index == 0:  # 删除的是头节点
            self.head = self.head.next
            if self.head is None:  # 如果链表变空
                self.tail = None
        else:  # 删除的是中间节点或尾节点
            previous = self._get_node(index - 1)
            previous.next = previous.next.next
            if previous.next is None:  # 删除的是尾节点
                self.tail = previous

        self._size -= 1

    def pop(self) -> Optional[T]:
        """移除并返回链表的最后一个元素"""
        if self.head is None:  # 如果链表为空
            return None
        if self.head.next is None:  # 如果链表只有一个元素
            pop_value = self.head.value
            self.head = self.tail = None  # 更新头节点和尾节点
            self._size -= 1
            return pop_value

        current = self.head
        while current.next.next:
            current = current.next
        pop_value = current.next.value
        current.next = None
        self.tail = current
        self._size -= 1
        return pop_value

    def find(self, target: T) -> int:
        """查找特定值 T 在链表中的位置"""
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, index: int) -> Optional[T]:
        """获取链表中指定索引位置的元素的值"""
        current = self._get_node(index)
        return current.value

    def is_empty(self) -> bool:
        """检查链表是否为空"""
        return self.head is None

    def size(self) -> int:
        """返回链表中元素的数量"""
        return self._size

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        """使链表可迭代"""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self) -> str:
        """返回链表的字符串表示"""
        return " -> ".join(str(value) for value in self)
