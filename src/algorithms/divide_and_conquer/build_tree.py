"""Build Tree

Question:
给定一棵二叉树的前序遍历 preorder 和中序遍历 inorder ，请从中构建二叉树，返回二叉树的根节点。假设二叉树中没有值重复的节点。

Answer:
1.  判断是否为分治问题
    - 问题可以分解
        从分治的角度切入，我们可以将原问题划分为两个子问题：构建左子树、构建右子树，加上一步操作：初始化根节点。而对于
        每棵子树（子问题），我们仍然可以复用以上划分方法，将其划分为更小的子树（子问题），直至达到最小子问题（空子树）
        时终止。
    - 子问题是独立的
        左子树和右子树是相互独立的，它们之间没有交集。在构建左子树时，我们只需关注中序遍历和前序遍历中与左子树对应的部
        分。右子树同理。
    - 子问题的解可以合并
        一旦得到了左子树和右子树（子问题的解），我们就可以将它们链接到根节点上，得到原问题的解。
2.  如何划分子树
    根据定义，preorder 和 inorder 都可以划分为 3 个部分。
    - 前序遍历：[ 根节点 | 左子树 | 右子树 ]
    - 中序遍历：[ 左子树 | 根节点 | 右子树 ]
    - 后序遍历：[ 左子树 | 右子树 | 根节点 ]
    由此可知
    1. 前序遍历的第一个元素必为根节点 -> root
    2. 中序遍历的结构：[ [左子树] - root - [右子树] ]
    3. 对左子树和右子树递归进行 1 和 2，直到为左子树和右子树为空
3.  基于变量描述子树区间
    根据以上划分方法，我们已经得到根节点、左子树、右子树在 preorder 和 inorder 中的索引区间。而为了描述这些索引区间，
    我们需要借助几个指针变量。
    - 当前树的根节点在 preorder 中的索引记为 i。
    - 当前树的根节点在 inorder 中的索引记为 m。
    - 当前树在 inorder 中的索引区间记为 [l, r]。
    通过上述变量即可表示根节点在 preorder 中的索引，以及子树在 inorder 中的索引区间。
|        | 根节点在 pre 中的索引 | 子树在 pre 中的索引区间 | 根节点在 in 中的索引 | 子树在 in 中的索引区间 | 区间长度 |
| :----: | :-----------: | :-------      -----------: | :--: | :--------: | :-------: |
| 当前树  | i             | [i, i + r - l]             | m    | [l, r]     | r - l + 1 |
| 左子树  | i + 1         | [i + 1, i + m - l]         | NULL | [l, m - 1] | m - l     |
| 右子树  | i + 1 + m - l | [i + 1 + m - l, i + r - l] | NULL | [m + 1, r] | r - m     |
4.  代码实现
为了提升查询 m 的效率，我们借助一个哈希表 hmap 来存储数组 inorder 中元素到索引的映射。
5.  代码分析
设树的节点个数为 n，则时间复杂度为 O(n)，空间复杂度为 O(n)。
"""
from __future__ import annotations

from src.data_structures.tree.binary_tree import TreeNode


def dfs(
        preorder: list[int],
        inorder_map: dict[int, int],
        i: int,
        l: int,
        r: int,
) -> TreeNode | None:
    """构建二叉树：分治"""
    # 子树为空时返回
    if r - l < 0:
        return None
    # 初始化根节点
    root = TreeNode(preorder[i])
    # 获取根节点在 inorder 中的索引
    m = inorder_map[preorder[i]]
    # 构建左子树
    root.left = dfs(preorder, inorder_map, i + 1, l, m - 1)
    # 构建右子树
    root.right = dfs(preorder, inorder_map, i + 1 + m - l, m + 1, r)
    # 返回根节点
    return root


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """构建二叉树"""
    # 初始化哈希表，存储 inorder 元素到索引映射
    inorder_map = {value: index for index, value in enumerate(inorder)}
    root = dfs(preorder, inorder_map, 0, 0, len(inorder) - 1)
    return root
