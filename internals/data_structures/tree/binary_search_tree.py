"""
「二叉搜索树（Binary Search Tree）」
1.  二叉搜索树满足以下条件
    a.  对于根节点，左子树中所有节点的值 < 根节点的值 < 右子树中所有节点的值。
    b.  任意节点的左、右子树也是二叉搜索树，即同样满足条件`1`。
2.  二叉搜索树不允许存在重复节点，否则将违反其定义。因此，若待插入节点在树中已存在，则不执行插入，直接返回。
3.  为了实现插入节点，我们需要借助节点 pre 保存上一轮循环的节点。这样在遍历至 None 时，我们可以获取到其父节点，从而完成节点插入操作。
4.  二叉搜索树的中序遍历是升序的
    a.  二叉树的中序遍历遵循“左 -> 根 -> 右”的遍历顺序，而二叉搜索树满足“左子节点 < 根节点 < 右子节点”的大小关系。这意味着在二叉搜索树
        中进行中序遍历时，总是会优先遍历下一个最小节点，从而得出一个重要性质：二叉搜索树的中序遍历序列是升序的。
    b.  利用中序遍历升序的性质，我们在二叉搜索树中获取有序数据仅需 O(n) 时间，无须进行额外的排序操作，非常高效。
5.  二叉搜索树的效率
    a.  二叉搜索树的各项操作的时间复杂度都是对数阶，具有稳定且高效的性能。只有在高频添加、低频查找删除数据的场景下，数组比二叉搜索树的效率更高。
    b.  理想情况下，二叉搜索树是“平衡”的，这样接可以在 log n 轮循环内查找任意节点。
    c.  如果在二叉搜索树中不断频繁的插入和删除节点，可能会导致二叉树退化为链表，各类操作的时间复杂度也会退化为 O(n)。
6.  二叉搜索树的应用
    a.  用作系统中的多级索引，实现高效的查找、插入、删除操作。
    b.  作为某些搜索算法的底层数据结构。
    c.  用于存储数据流，以保持其有序状态。
"""
from __future__ import annotations

from typing import TypeVar, Generic, Optional

from internals.data_structures.tree.binary_tree import TreeNode

T = TypeVar('T')


class BinarySearchTree(Generic[T]):
    """二叉查找树"""

    def __init__(self):
        self._root: Optional[TreeNode[T]] = None

    def search(self, target: T) -> Optional[TreeNode[T]]:
        """查找节点
        1.  二叉搜索树的查找操作与二分查找算法的工作原理一致，都是每轮排除一半情况。
        2.  循环次数最多为二叉树的高度，当二叉树平衡时，使用 O(log n) 时间。
        """
        # TODO: 是否应该设置 flag，在未找到时候异常/仅仅保持现状，未找到则返回 None
        current = self._root
        while current is not None:
            # 目标节点在当前节点的左子树中
            if target < current.value:
                current = current.left
            # 目标节点在当前节点的右子树中
            elif target > current.value:
                current = current.right
            # 找到目标节点，跳出循环
            else:
                break
        return current

    def insert(self, target: T):
        """插入节点
        1.  插入节点的操作流程
        2.  插入节点使用 O(log n) 时间。
        """
        # 若树为空，则初始化根节点
        if self._root is None:
            self._root = TreeNode(target)
            return

        # 若树不为空，则查找适合插入元素 target 的位置
        cur, pre = self._root, None
        while cur is not None:
            if target == cur.value:
                return  # 若 target 是重复节点，则可直接返回
            pre = cur  # 记录当前节点
            if target < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        # 在合适位置插入节点
        tree_node = TreeNode(target)
        if target < pre.value:
            pre.left = tree_node
        else:
            pre.right = tree_node

    def remove(self, target: T):
        """删除节点
        1.  删除节点的操作流程
            - 在二叉树中查找到目标节点。
            - 将目标节点删除。
        2.  删除操作完成后，需要保证二叉搜索树的“左子树 < 根节点 < 右子树”的性质仍然满足。因此，我们根据目标节点的
            子节点数量，分 0、1 和 2 三种情况，执行对应的删除节点操作。
            - 当目标节点的度为 0 时，说明该节点为叶节点，直接删除即可。
            - 当目标节点的度为 1 时，将待删除节点替换为其子节点即可。
            - 当目标节点的度为 2 时，需要一个节点来替换待删除节点，该节点可能为待删除节点的左子树的最大值或者右子树
              的最小值。
        3.  当待删除节点的度为 2 时，假设选择「右子树的最小节点（中序遍历的下一个节点）」替换待删除节点，则需要：
            - 找到待删除节点在「中序遍历序列」中的下一个节点，记为 temp。
            - 用 temp 的值覆盖待删除节点的值，并在树中递归删除节点 temp。
        4   删除节点操作同样使用 O(log n) 时间，其中查找待删除节点需要 O(log n) 时间，获取中序遍历后继节点需要 O(log n) 时间。
        """
        # 若树为空，则直接返回
        if self._root is None:
            return

        # 若树不为空，则查找需要删除的节点
        cur, pre = self._root, None
        while cur is not None:
            if target == cur.value:
                break
            pre = cur
            if target < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        # 若 cur == None，则说明未找到要删除的 target，直接返回
        if cur is None:
            return

        # 若 cur != None，则说明已找到要删除的 target，执行删除
        if cur.left is None or cur.right is None:  # 待删除节点的度为 0 或者 1
            child = cur.left or cur.right
            if cur != self._root:  # 若待删除节点不是根节点，则执行删除操作
                if cur == pre.left:
                    pre.left = child
                else:
                    pre.right = child
            else:  # 若待删除节点为根节点，则重新指定根节点
                self._root = child
        else:  # 待删除节点的度为 2，寻找右子树的最小值
            temp = cur.right
            while temp.left is not None:
                temp = temp.left
            # 递归删除 temp
            self.remove(temp.value)
            # 覆盖待删除节点的值
            cur.value = temp.value
