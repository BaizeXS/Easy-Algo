from __future__ import annotations
from typing import TypeVar, Generic, Optional, Iterator

T = TypeVar('T')


class BiNode:
    """双向链表节点的基类"""

    def __init__(self):
        self.prev: Optional[BiNode] = None
        self.next: Optional[BiNode] = None


class SentinelNode(BiNode):
    """哨兵节点类"""
    pass


class BiListNode(BiNode, Generic[T]):
    """双向链表节点类"""

    def __init__(self,
                 value: T,
                 prev_node: Optional[SentinelNode | BiListNode[T]] = None,
                 next_node: Optional[SentinelNode | BiListNode[T]] = None):
        super().__init__()
        self.value: T = value
        self.prev: Optional[SentinelNode | BiListNode[T]] = prev_node
        self.next: Optional[SentinelNode | BiListNode[T]] = next_node

    def __repr__(self) -> str:
        return f"BiListNode({self.value})"


class BiLinkedList(Generic[T]):
    """双向链表类"""

    def __init__(self):
        self.head: SentinelNode = SentinelNode()  # 创建哨兵头节点
        self.tail: SentinelNode = SentinelNode()  # 创建哨兵尾节点
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def append(self, value: T):
        """在链表尾部添加一个新元素"""
        node = BiListNode(value, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self._size += 1

    def prepend(self, value: T):
        """在链表头部添加一个新元素"""
        node = BiListNode(value, self.head, self.head.next)
        self.head.next.prev = node
        self.head.next = node
        self._size += 1

    def insert(self, index: int, value: T):
        """在索引 index 处插入元素"""
        if not isinstance(index, int):
            raise TypeError("索引必须是整数")

        if index == 0:
            self.prepend(value)
            return
        elif index == self._size:
            self.append(value)
            return
        else:
            current = self._get_node(index)
            node = BiListNode(value, current.prev, current)
            current.prev.next = node
            current.prev = node
            self._size += 1

    def _get_node(self, index: int) -> BiListNode[T]:
        """获取指定索引处的节点"""
        if index < 0:  # 添加对负数索引的支持
            index += self._size

        if index < 0 or index >= self._size:
            raise IndexError("索引越界")

        # 优化遍历效率
        if index < self._size // 2:
            current = self.head.next
            for _ in range(index):
                current = current.next
        else:
            current = self.tail.prev
            for _ in range(self._size - index - 1):
                current = current.prev

        return current

    def delete(self, value: T):
        """删除链表中第一个值为 value 的节点"""
        current = self.head.next
        while isinstance(current, BiListNode):
            if current.value == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                current.prev = None  # 断开引用，帮助垃圾回收
                current.next = None  # 断开引用，帮助垃圾回收
                self._size -= 1
                return
            current = current.next

    def delete_at(self, index: int):
        """删除链表中索引为 index 的节点"""
        current = self._get_node(index)
        current.prev.next = current.next
        current.next.prev = current.prev
        current.prev = None
        current.next = None
        self._size -= 1

    def pop(self) -> Optional[T]:
        """移除并返回链表的最后一个元素"""
        if self._size == 0:
            raise IndexError("从空链表中弹出元素")

        last_node = self.tail.prev
        if not isinstance(last_node, BiListNode):
            raise RuntimeError("内部错误：链表的最后一个节点不是 BiListNode")

        pop_value = last_node.value
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev
        last_node.prev = None  # 断开引用，帮助垃圾回收
        last_node.next = None  # 断开引用，帮助垃圾回收
        self._size -= 1

        return pop_value

    def find(self, target: T) -> int:
        """查找特定值在链表中的位置"""
        for index, value in enumerate(self):
            if value == target:
                return index
        return -1

    def get(self, index: int) -> T:
        """获取链表中指定索引位置的元素的值"""
        current = self._get_node(index)
        return current.value

    def is_empty(self) -> bool:
        """检查链表是否为空"""
        return self._size == 0

    def size(self) -> int:
        """返回链表中元素的数量"""
        return self._size

    def __len__(self) -> int:
        """返回链表长度"""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """使链表可迭代"""
        current = self.head.next
        while isinstance(current, BiListNode):
            yield current.value
            current = current.next

    def __str__(self) -> str:
        """返回链表的字符串表示"""
        return " <-> ".join(str(value) for value in self)
