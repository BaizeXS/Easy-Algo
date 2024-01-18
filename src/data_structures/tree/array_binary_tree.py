"""
二叉树数组表示


表示完美二叉树

1.  给定一棵完美二叉树，我们将所有节点按照层序遍历的顺序存储在一个数组中，则每个节点都对应唯一的数组索引。
2.  根据层序遍历的特性，我们可以推导出父节点索引与子节点索引之间的“映射公式”：
    若某节点的索引为 i，则该节点的左子节点索引为 2i + 1，右子节点索引为 2i + 2。


表示任意二叉树

1.  完美二叉树是一个特例，在二叉树的中间层通常存在许多 None。由于层序遍历序列并不包含这些 None，因此我们无法
    仅凭该序列来推测 None 的数量和分布位置。这意味着存在多种二叉树结构都符合该层序遍历序列。为了解决此问题，
    **我们可以考虑在层序遍历序列中显式地写出所有 None。**
2.  值得说明的是，完全二叉树非常适合使用数组来表示。回顾完全二叉树的定义，None 只出现在最底层且靠右的位置，因
    此所有 None 一定出现在层序遍历序列的末尾。


数组表示二叉树的优点与局限性

1.  优点
    - 数组存储在连续的内存空间中，对缓存友好，访问与遍历速度较快。
    - 不需要存储指针，比较节省空间。
    - 允许随机访问节点。
2.  局限性
    - 数组存储需要连续内存空间，因此不适合存储数据量过大的树。
    - 增删节点需要通过数组插入与删除操作实现，效率较低。
    - 当二叉树中存在大量 None 时，数组中包含的节点数据比重较低，空间利用率较低。
"""
from __future__ import annotations

from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class ArrayBinaryTree(Generic[T]):
    """基于数组实现的二叉树"""

    MAX_CAPACITY = 512

    def __init__(self, capacity: int = 16):
        if not 0 <= capacity <= ArrayBinaryTree.MAX_CAPACITY:
            raise ValueError(f"容量必须在0到最大容量 {ArrayBinaryTree.MAX_CAPACITY} 之间")
        self._tree: list[Optional[T]] = [None] * capacity
        self._capacity: int = capacity
        self._size: int = 0

    @property
    def capacity(self) -> int:
        """返回二叉树的容量"""
        return self._capacity

    @property
    def size(self) -> int:
        """返回二叉树中的节点数量"""
        return self._size

    def _ensure_capacity(self):
        """如果需要，扩展数组以确保足够的容量"""
        if self._size < self._capacity:
            return

        if self._capacity >= ArrayBinaryTree.MAX_CAPACITY:
            raise Exception(f"二叉树达到最大容量 {ArrayBinaryTree.MAX_CAPACITY}。")

        new_capacity = min(self._capacity * 2, ArrayBinaryTree.MAX_CAPACITY)
        self._tree.extend([None] * (new_capacity - self._capacity))
        self._capacity = new_capacity

    def insert(self, value: T) -> bool:
        """在二叉树第一个空闲位置插入元素"""
        self._ensure_capacity()
        for i, tree_node in enumerate(self._tree):
            if tree_node is None:
                self._tree[i] = value
                self._size += 1
                return True
        return False

    def search(self, value: T) -> bool:
        """在二叉树中搜索元素是否存在"""
        return value in self._tree

    def remove(self, value: T) -> bool:
        """在二叉树中移除元素"""
        for i, tree_node in enumerate(self._tree):
            if tree_node == value:
                self._tree[i] = None
                self._size -= 1
                return True
        return False

    def value(self, index: int) -> Optional[T]:
        """获取指定索引处的节点值"""
        if 0 <= index < self._capacity:
            return self._tree[index]
        raise IndexError("索引越界")

    def parent(self, index: int) -> Optional[int]:
        """获取指定索引节点的父节点索引"""
        if 0 < index < self._capacity:  # 节点索引大于 0 时才存在父节点
            return (index - 1) // 2
        return None

    def left(self, index: int) -> Optional[int]:
        """获取指定索引节点的左子节点索引"""
        left_index: int = index * 2 + 1
        return left_index if left_index < self._capacity else None

    def right(self, index: int) -> Optional[int]:
        """获取指定索引节点的右子节点索引"""
        right_index = 2 * index + 2
        return right_index if right_index < self._capacity else None

    def level_order_traversal(self) -> list[Optional[T]]:
        """层序遍历"""
        return [self._tree[i] for i in range(self._capacity) if self._tree[i] is not None]

    def _dfs(self, index: int, order: str, res: list[Optional[T]]):
        """深度优先遍历的辅助函数"""
        if index is None or self.value(index) is None:
            return

        # TODO: 若 left 和 right 为 None 时应该加入异常处理
        left_index = self.left(index)
        right_index = self.right(index)

        if order == "pre":
            res.append(self.value(index))
        if left_index is not None:
            self._dfs(left_index, order, res)
        if order == "in":
            res.append(self.value(index))
        if right_index is not None:
            self._dfs(right_index, order, res)
        if order == "post":
            res.append(self.value(index))

    def pre_order_traversal(self) -> list[Optional[T]]:
        """前序遍历"""
        res = []
        self._dfs(0, "pre", res)
        return res

    def in_order_traversal(self) -> list[Optional[T]]:
        """中序遍历"""
        res = []
        self._dfs(0, "in", res)
        return res

    def post_order_traversal(self) -> list[Optional[T]]:
        """后序遍历"""
        res = []
        self._dfs(0, "post", res)
        return res
