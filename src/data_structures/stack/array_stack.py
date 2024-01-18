from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class ArrayStack(Generic[T]):
    """基于数组实现的栈"""

    def __init__(self, capacity: Optional[int] = None) -> None:
        """构造方法"""
        self._stack: list[T] = []
        self._capacity: Optional[int] = capacity

    def peek(self) -> T:
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError('栈为空')
        return self._stack[-1]

    def push(self, val: T):
        """入栈操作"""
        if self._capacity is not None and len(self._stack) >= self._capacity:
            raise OverflowError('栈已满，无法添加新元素')
        self._stack.append(val)

    def pop(self) -> T:
        """出栈操作"""
        if self.is_empty():
            raise IndexError('栈为空，无法弹出元素')
        return self._stack.pop()

    def clear(self):
        """清空栈"""
        self._stack.clear()

    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return len(self._stack) == 0

    def size(self) -> int:
        """获取栈的长度"""
        return len(self._stack)

    def copy(self) -> ArrayStack[T]:
        """复制当前栈"""
        new_stack = ArrayStack[T](self._capacity)
        new_stack._stack = self._stack.copy()
        return new_stack

    def __str__(self):
        """字符串表示"""
        return str(self._stack)
