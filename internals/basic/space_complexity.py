class Node:
    """类"""

    def __init__(self, x: int):
        self.val: int = x  # 节点值
        self.next: Node | None = None  # 指向下一节点的引用


def function() -> int:
    # 执行某些操作...
    return 0


def loop(n: int):
    """循环 O(1)"""
    for _ in range(n):
        function()


def recur(n: int) -> int:
    """递归 O(n)"""
    if n == 1:
        return
    return recur(n - 1)


def constant(n: int):
    """常数阶"""
    # 常量、变量、对象占用 O(1) 空间
    a = 0
    nums = [0] * 10000
    node = Node(0)
    # 循环中的变量占用 O(1) 空间
    for _ in range(n):
        c = 0
    # 循环中的函数占用 O(1) 空间
    for _ in range(n):
        function()


def linear(n: int):
    """线性阶"""
    # 长度为 n 的列表占用 O(n) 空间
    nums = [0] * n
    # 长度为 n 的哈希表占用 O(n) 空间
    hmap = dict[int, str]()
    for i in range(n):
        hmap[i] = str(i)


def linear_recur(n: int):
    """线性阶（递归实现）"""
    print("递归 n =", n)
    if n == 1:
        return
    return linear_recur(n - 1)


def quadratic(n: int):
    """平方阶：平方阶常见于矩阵和图"""
    # 二维列表占用 O(n^2) 空间
    num_matrix = [[0] * n for _ in range(n)]


def quadratic_recur(n: int) -> int:
    """平方阶（递归实现）"""
    if n <= 0:
        return 0
    nums = [0] * n
    return quadratic_recur(n - 1)


# 对数阶常见于分治算法。例如归并排序等。
# def build_tree(n: int) -> TreeNode | None:
#     """指数阶（建立满二叉树）"""
#     if n == 0:
#         return None
#     root = TreeNode(0)
#     root.get_left_index = build_tree(n - 1)
#     root.get_right_index = build_tree(n - 1)
#     return root
