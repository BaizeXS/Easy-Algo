# 初始化二叉树
from internals.data_structures.tree.binary_tree import TreeNode

n1 = TreeNode(value=1)
n2 = TreeNode(value=2)
n3 = TreeNode(value=3)
n4 = TreeNode(value=4)
n5 = TreeNode(value=5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

# 插入与删除节点
p = TreeNode(value=0)
# 在 n1 -> n2 中间插入节点 P
n1.left = p
p.left = n2
# 删除节点 P
# 需要注意的是，插入节点可能会改变二叉树的原有逻辑结构，而删除节点通常意味着删除该节点及其所有子树。
# 因此，在二叉树中，插入与删除通常是由一套操作配合完成的，以实现有实际意义的操作。
n1.left = n2

# 二叉树的数组表示
# 使用 None 来表示空位
tree = [1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15]
