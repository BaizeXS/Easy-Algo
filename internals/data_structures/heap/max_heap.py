"""
Max Heap implementation

1.  堆是一种特殊的完全二叉树，非常适合使用数组表示，因此我们使用数组来存储堆。
2.  使用数组表示二叉树时，元素代表节点值，索引代表节点在二叉树中的位置。
3.  节点指针通过索引映射公式实现，给定索引 i：
        - 左子节点索引： 2 * i + 1
        - 右子节点索引： 2 * i + 2
        - 父节点索引： (i - 1) // 2
    当索引越界时，表示空节点或者节点不存在。
"""
from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class MaxHeap(Generic[T]):

    def __init__(self):
        pass

    def left_index(self, index: int) -> int:
        """获取左子节点索引"""
        return 2 * index + 1

    def right_index(self, index: int) -> int:
        """获取右子节点索引"""
        return 2 * index + 2

    def parent_index(self, index: int) -> int:
        """获取父节点索引"""
        return (index - 1) // 2
