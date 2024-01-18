"""
栈
"""
from __future__ import annotations
from typing import TypeVar, Generic, Optional, Iterator

from src.data_structures.linked_list.linked_list import ListNode

T = TypeVar('T')


class LinkedListStack(Generic[T]):
    """基于链表的实现"""

    def __init__(self, capacity: Optional[int] = None) -> None:
        """构造方法"""
        self._peek: Optional[ListNode[T]] = None
        self._size: int = 0
        self._capacity: Optional[int] = capacity

    def peek(self) -> T:
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.value

    def push(self, value: T) -> None:
        """入栈操作"""
        if self._capacity is not None and self._size >= self._capacity:
            raise OverflowError("栈溢出")
        self._peek = ListNode(value, self._peek)
        self._size += 1

    def pop(self) -> T:
        """出栈操作"""
        if self.is_empty():
            raise IndexError("栈为空")
        pop_value = self._peek.value
        self._peek = self._peek.next
        self._size -= 1
        return pop_value

    def clear(self) -> None:
        """清空栈"""
        self._peek = None
        self._size = 0

    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return self._size == 0

    def size(self) -> int:
        """返回栈的长度"""
        return self._size

    def copy(self) -> LinkedListStack[T]:
        """复制当前栈"""
        new_stack = LinkedListStack(self._capacity)
        temp_list = list(self)
        for i in range(self._size - 1, -1, -1):
            new_stack.push(temp_list[i])
        return new_stack

    def __iter__(self) -> Iterator[T]:
        current = self._peek
        while current:
            yield current.value
            current = current.next

    def __str__(self) -> str:
        """字符串表示"""
        return f"Stack([{', '.join(str(value) for value in self)}])"
