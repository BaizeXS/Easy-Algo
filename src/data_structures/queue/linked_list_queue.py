from __future__ import annotations
from typing import TypeVar, Generic, Optional, Iterator

from src.data_structures.linked_list.linked_list import ListNode

T = TypeVar('T')


class LinkedListQueue(Generic[T]):
    """
    基于单链表实现的队列。

    方法:
    push(value: T): 将值添加到队列尾部。
    pop() -> T: 从队列前端移除并返回值。
    peek() -> T: 返回队列前端的值，但不移除它。
    is_empty() -> bool: 检查队列是否为空。
    size() -> int: 返回队列中的元素数量。
    """

    def __init__(self):
        """初始化一个空队列。"""
        self._front: Optional[ListNode[T]] = None
        self._rear: Optional[ListNode[T]] = None
        self._size: int = 0

    def peek(self) -> T:
        """返回队列前端的元素，但不移除它。"""
        if self._front is None:
            raise IndexError('队列为空，无法查看元素。')
        return self._front.value

    def push(self, value: T):
        """将元素添加到队列尾部。"""
        node = ListNode(value)
        if self.is_empty():
            self._front = self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def pop(self) -> T:
        """从队列前端移除并返回元素。"""
        if self._front is None:
            raise IndexError('无法从空队列中弹出元素。')
        pop_value = self._front.value
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return pop_value

    def clear(self) -> None:
        self._front = None
        self._rear = None
        self._size = 0

    def is_empty(self) -> bool:
        """检查队列是否为空。"""
        return self._size == 0

    def size(self) -> int:
        """返回队列的元素数量。"""
        return self._size

    def __len__(self):
        """返回队列的长度。"""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """使得队列可迭代"""
        current = self._front
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        """返回队列的字符串表示"""
        return f"LinkedListQueue([{', '.join(str(value) for value in self)}])"
