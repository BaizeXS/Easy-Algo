"""
AVL Tree

旋转的选择

    失衡节点的平衡因子       子节点的平衡因子        应该采用的旋转方法
    > 1  (左偏树)          >= 0                    右旋
    > 1  (左偏树)          < 0                     先左旋后右旋
    < -1 (右偏树)          <= 0                    左旋
    < -1 (右偏树)          > 0                     先右旋后左旋


AVL 树的典型应用

- 组织和存储大型数据，适用于高频查找、低频增删的场景。
- 用于构建数据库中的索引系统。
- 红黑树在许多应用中比 AVL 树更受欢迎。这是因为红黑树的平衡条件相对宽松，在红黑树中插入与删除节点所需的旋转操作相对较少，其节点增删操作的平均效率更高。
"""
from __future__ import annotations

from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class AVLTreeNode(Generic[T]):

    def __init__(self, value: T):
        self.value = value  # 节点值
        self.height: int = 0  # 节点高度
        self.left: Optional[AVLTreeNode[T]] = None  # 左子节点引用
        self.right: Optional[AVLTreeNode[T]] = None  # 右子节点引用


class AVLTree(Generic[T]):
    """AVL树类"""

    def __init__(self):
        self._root: Optional[AVLTreeNode[T]] = None

    def is_empty(self) -> bool:
        """检查树是否为空"""
        return self._root is None

    def size(self) -> int:
        """返回树中的节点数"""

        def _size(node: Optional[AVLTreeNode[T]]) -> int:
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self._root)

    def get_height(self, node: Optional[AVLTreeNode[T]]) -> int:
        """获取节点高度"""
        # 空节点高度为 -1，叶节点高度为 0
        if node is not None:
            return node.height
        return -1

    def update_height(self, node: Optional[AVLTreeNode[T]]):
        """更新节点高度"""
        # 节点高度等于最高子树高度 + 1
        node.height = max([self.get_height(node.left), self.get_height(node.right)]) + 1

    def balance_factor(self, node: Optional[AVLTreeNode[T]]):
        """获取平衡因子"""
        # 空节点的平衡因子为 0
        if node is None:
            return 0
        # 节点平衡因子 = 左子树高度 - 右子树高度
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node: Optional[AVLTreeNode[T]]) -> Optional[AVLTreeNode[T]]:
        """右旋操作"""
        # 记录 child 节点和 grand child 节点
        child = node.left
        grand_child = child.right
        # 以 child 为原点，将 node 向右旋转
        child.right = node
        node.left = grand_child
        # 更新节点高度
        self.update_height(node)
        self.update_height(child)

        return child

    def left_rotate(self, node: Optional[AVLTreeNode[T]]) -> Optional[AVLTreeNode[T]]:
        """左旋操作"""
        child = node.right
        grand_child = child.left

        child.left = node
        node.right = grand_child

        self.update_height(node)
        self.update_height(child)

        return child

    def rotate(self, node: Optional[AVLTreeNode[T]]) -> Optional[AVLTreeNode[T]]:
        """执行旋转操作，使该子树重新恢复平衡"""
        balance_factor = self.balance_factor(node)
        # 左偏树
        if balance_factor > 1:
            # 右旋
            if self.balance_factor(node.left) >= 0:
                return self.right_rotate(node)
            # 先左旋后右旋
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        # 右偏树
        elif balance_factor < -1:
            # 左旋
            if self.balance_factor(node.right) <= 0:
                return self.left_rotate(node)
            # 先右旋后左旋
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        # 平衡树，无需旋转，直接返回
        return node

    def insert(self, value: T):
        """插入节点
        AVL 树的节点插入操作与二叉搜索树在主体上类似。唯一的区别在于，在 AVL 树中插入节点后，
        从该节点到根节点的路径上可能会出现一系列失衡节点。因此，我们需要从这个节点开始，自底向
        上执行旋转操作，使所有失衡节点恢复平衡。
        """

        def _insert(_node: Optional[AVLTreeNode[T]], _value: T) -> AVLTreeNode[T]:
            """插入节点辅助函数——递归插入节点"""
            if _node is None:
                return AVLTreeNode(_value)
            # 查找合适的插入节点
            if _value < _node.value:
                _node.left = _insert(_node.left, _value)
            elif _value > _node.value:
                _node.right = _insert(_node.right, _value)
            else:
                # 重复节点不插入，直接返回
                return _node
            # 更新节点高度
            self.update_height(_node)
            # 执行旋转操作，保证 AVL 树的平衡
            return self.rotate(_node)

        self._root = _insert(self._root, value)

    def remove(self, value: T):
        """删除节点"""

        def _remove(_node: Optional[AVLTreeNode[T]], _value: T) -> Optional[AVLTreeNode[T]]:
            """删除节点辅助函数"""
            if _node is None:
                return None
            # 查找要删除的节点
            if _value < _node.value:
                _node.left = _remove(_node.left, _value)
            elif _value > _node.value:
                _node.right = _remove(_node.right, _value)
            else:
                # 节点的度为 0 或 1
                if _node.left is None or _node.right is None:
                    child = _node.left or _node.right
                    if child is None:  # 节点度为 0，直接删除 node 并返回
                        return None
                    else:  # 节点度为 1，直接删除 node
                        _node = child
                # 节点的度为 2
                else:
                    # 子节点数量 = 2 ，则将中序遍历的下个节点删除，并用该节点替换当前节点
                    temp = _node.right
                    while temp.left is not None:
                        temp = temp.left
                    _node.right = _remove(_node.right, temp.value)
                    _node.value = temp.value
            # 更新节点高度
            self.update_height(_node)
            # 执行旋转操作，保证 AVL 树的平衡
            return self.rotate(_node)

        self._root = _remove(self._root, value)

    def search(self, value: T) -> bool:
        """查找节点"""

        def _search(_node: Optional[AVLTreeNode[T]], _value: T) -> bool:
            """查找节点辅助函数"""
            if _node is None:
                return False
            if _value < _node.value:
                return _search(_node.left, _value)
            elif _value > _node.value:
                return _search(_node.right, _value)
            else:
                return True

        return _search(self._root, value)
