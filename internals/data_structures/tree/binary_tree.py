"""
常见的二叉树类型

1.  完美二叉树（满二叉树）：叶节点的度为0，其余节点度均为2；若树的高度为 h，则节点总数为 2^(h + 1) - 1。
2.  完全二叉树：只有最底层的节点未被填满，且最底层节点尽量靠左填充。
3.  完满二叉树：除了叶节点之外，其余节点都有两个子节点（所有节点的度为0或2）。
4.  平衡二叉树：任意节点左子树和右子树的高度之差的绝对值不超过1。


二叉树的退化

当所有节点偏向一侧时，二叉树退化成链表，时间复杂度退化至 O(n)。


二叉树遍历

1.  二叉树常见的遍历方式包括层序遍历、前序遍历、中序遍历和后序遍历等。
    层序遍历本质上属于「广度优先遍历（Breadth-First Traversal，BFS）」，它体现了一种“一圈一圈向外扩展”的逐层遍历方式。
    前序、中序、后序遍历都属于「深度优先遍历（Depth-First Traversal，DFS）」，它体现了一种“先走到尽头，再回溯继续”的遍历方式。
2.  层序遍历
    广度优先遍历通常借助“队列”来实现。队列遵循“先进先出”的规则，而广度优先遍历则遵循“逐层推进”的规则，两者背后的思想是一致的。
3.  前序遍历
4.  中序遍历
5.  后序遍历
"""
from typing import TypeVar, Generic, Optional

from internals.data_structures.queue.usage import deque

T = TypeVar('T')


class TreeNode(Generic[T]):
    """二叉树节点类"""

    def __init__(self, value: T):
        self.value = value  # 节点值
        self.left: Optional[TreeNode[T]] = None  # 左子节点引用
        self.right: Optional[TreeNode[T]] = None  # 右子节点引用


# 广度优先遍历 -> 层序遍历
def level_order(root: Optional[TreeNode[T]]) -> list[T]:
    """层序遍历"""
    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.value)  # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right)  # 右子节点入队
    return res


# 深度优先遍历 -> 前序、中序、后序遍历
result = []


def pre_order(root: Optional[TreeNode[T]]):
    """前序遍历"""
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    result.append(root.value)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root: Optional[TreeNode[T]]):
    """中序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root.left)
    result.append(root.value)
    in_order(root.right)


def post_order(root: Optional[TreeNode[T]]):
    """后序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root.left)
    post_order(root.right)
    result.append(root.value)
