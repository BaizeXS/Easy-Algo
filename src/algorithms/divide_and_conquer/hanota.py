"""汉诺塔问题
Question：
给定三根柱子，记为 A、B 和 C。起始状态下，柱子 A 上套着 n 个圆盘，它们从上到下按照从小到大的顺序排列。我们的任务是
要把这 n 个圆盘移到柱子 C 上，并保持它们的原有顺序不变。在移动圆盘的过程中，需要遵守以下规则。
- 圆盘只能从一根柱子顶部拿出，从另一根柱子顶部放入。
- 每次只能移动一个圆盘。
- 小圆盘必须时刻位于大圆盘之上。

Answer：
将原问题 f(n) 划分为两个子问题 f(n - 1) 和一个子问题 f(1)，并按照以下顺序解决这三个子问题。
1.  将 n - 1 个圆盘借助 C 从 A 移至 B。
2.  将剩余 1 个圆盘从 A 直接移至 C。
3.  将 n - 1 个圆盘借助 A 从 B 移至 C。

时间复杂度：O(2^n)
空间复杂度：O(n)
https://www.hello-algo.com/chapter_divide_and_conquer/hanota_problem
"""


def move(src: list[int], tar: list[int]):
    """移动一个圆盘"""
    disk = src.pop()
    tar.append(disk)


def dfs(i: int, src: list[int], buf: list[int], tar: list[int]):
    """求解汉诺塔问题 f(i)"""
    # 若 src 只剩下一个圆盘，则直接将其移到 tar
    if i == 1:
        move(src, tar)
        return
    # 子问题 f(i-1) ：将 src 顶部 i-1 个圆盘借助 tar 移到 buf
    dfs(i - 1, src, tar, buf)
    # 子问题 f(1) ：将 src 剩余一个圆盘移到 tar
    move(src, tar)
    # 子问题 f(i-1) ：将 buf 顶部 i-1 个圆盘借助 src 移到 tar
    dfs(i - 1, buf, src, tar)


def solve_hanota(a: list[int], b: list[int], c: list[int]):
    """求解汉诺塔问题"""
    n = len(a)
    dfs(n, a, b, c)


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    B = []
    C = []
    solve_hanota(A, B, C)
    print(A)
    print(B)
    print(C)
