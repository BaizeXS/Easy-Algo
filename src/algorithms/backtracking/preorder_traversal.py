"""
例题一：给定一颗二叉树，搜索并记录所有值为 7 个节点，请返回节点列表。

例题二：在二叉树中搜索所有值为 7 的节点，请返回根节点到这些节点的路径。

例题三：在二叉树中搜索所有值为 7 的节点，请返回根节点到这些节点的路径，并要求路径中不包含值为 3 的节点。
"""
from src.data_structures.tree.binary_tree import TreeNode

res = []
path = []


def pre_order_traversal_i(root: TreeNode):
    """前序遍历：例题一"""
    if root is None:
        return
    if root.value == 7:
        res.append(root)
    pre_order_traversal_i(root.left)
    pre_order_traversal_i(root.right)


def pre_order_traversal_ii(root: TreeNode):
    """
    在例题一代码的基础上，我们需要借助一个列表 path 记录访问过的节点路径。当访问到值为 7 的节点时，则复制 path
    并添加进结果列表 res。遍历完成后，res中保存的就是所有解。
    """
    if root is None:
        return
    # 尝试
    path.append(root)
    if root.value == 7:
        res.append(list(path))
    pre_order_traversal_ii(root.left)
    pre_order_traversal_ii(root.right)
    # 回退
    path.pop()


def pre_order_traversal_iii(root: TreeNode):
    """
    为了满足以上约束条件，我们需要添加剪枝操作：在搜索过程中，若遇到值为 3 的节点，则提前返回，不再继续搜索。
    """
    if root is None or root.value == 3:
        return
    path.append(root)
    if root.value == 7:
        res.append(list(path))
    pre_order_traversal_iii(root.left)
    pre_order_traversal_iii(root.right)
    # 回退
    path.pop()

