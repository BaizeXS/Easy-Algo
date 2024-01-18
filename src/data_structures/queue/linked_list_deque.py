"""
双向队列

- 在队列中，我们仅仅能删除头部元素或在尾部添加元素，双向队列提供了更高的灵活性，允许在头部和尾部执行元素的添加和删除操作。
- 双向队列的常用操作
    - pushFirst()       将元素添加至队首        O(1)
    - pushLast()        将元素添加至队尾        O(1)
    - popFirst()        删除队首元素          O(1)
    - popLast()         删除队尾元素          O(1)
    - peekFirst()       访问队首元素          O(1)
    - peekLast()        访问队尾元素          O(1)
"""
from __future__ import annotations
from typing import TypeVar, Generic, Iterator

from src.data_structures.linked_list.bi_linked_list import SentinelNode, BiListNode

T = TypeVar('T')


class LinkedListDeque(Generic[T]):
    """基于双向链表实现的双向队列"""

    def __init__(self):
        self._front: SentinelNode = SentinelNode()
        self._rear: SentinelNode = SentinelNode()
        self._front.next = self._rear
        self._rear.prev = self._front
        self._size: int = 0

    def push_first(self, value: T):
        """在队首添加元素"""
        node = BiListNode(value, self._front, self._front.next)
        self._front.next.prev = node
        self._front.next = node
        self._size += 1

    def push_last(self, value: T):
        """在队尾添加元素"""
        node = BiListNode(value, self._rear.prev, self._rear)
        self._rear.prev.next = node
        self._rear.prev = node
        self._size += 1

    def pop_first(self) -> T:
        """删除队首元素"""
        pop_value = self.peek_first()

        pop_node = self._front.next
        self._front.next = pop_node.next
        pop_node.next.prev = self._front
        pop_node.prev = None  # 断开链接
        pop_node.next = None  # 断开链接
        self._size -= 1

        return pop_value

    def pop_last(self) -> T:
        """删除队尾元素"""
        pop_value = self.peek_last()

        pop_node = self._rear.prev
        self._rear.prev = pop_node.prev
        pop_node.prev.next = self._rear
        pop_node.prev = None  # 断开链接
        pop_node.next = None  # 断开链接
        self._size -= 1

        return pop_value

    def peek_first(self) -> T:
        """查看队首元素"""
        if self.is_empty():
            raise IndexError('双向队列为空')

        first_node = self._front.next
        if not isinstance(first_node, BiListNode):
            raise RuntimeError("内部错误：队列首部不是有效的数据节点")

        return first_node.value

    def peek_last(self) -> T:
        """查看队尾元素"""
        if self.is_empty():
            raise IndexError('双向队列为空')

        last_node = self._rear.prev
        if not isinstance(last_node, BiListNode):
            raise RuntimeError("内部错误：队列尾部不是有效的数据节点")

        return last_node.value

    def is_empty(self) -> bool:
        """检查队列是否为空"""
        return self._front.next == self._rear

    def size(self) -> int:
        """获取队列大小"""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """使队列可以迭代"""
        current = self._front.next
        while isinstance(current, BiListNode):
            yield current.value
            current = current.next

    def __str__(self):
        """字符串表示方法，用于打印队列内容"""
        values = [str(value) for value in self]
        return f"LinkedListDeque([" + ", ".join(values) + "])"
