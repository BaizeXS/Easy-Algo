def recur(n: int) -> int:
    """递归"""
    # 终止条件
    if n == 1:
        return 1
    # 递：递归调用
    res = recur(n - 1)
    # 归：返回结果
    return n + res


def tail_recur(n, res):
    # 终止条件
    if n == 0:
        return res
    # 尾递归调用
    return tail_recur(n - 1, res + n)


def fib(n: int) -> int:
    """斐波那契数列：递归
    观察以下代码，我们在函数内递归调用了两个函数，这意味着从一个调用产生了两个调用分支。
    这样不断递归调用下去，最终将产生一个层数为 n 的「递归树 recursion tree」。
    本质上看，递归体现“将问题分解为更小子问题”的思维范式，这种分治策略是至关重要的。
    - 从算法角度看，搜索、排序、回溯、分治、动态规划等许多重要算法策略都直接或间接地应用这种思维方式。
    - 从数据结构角度看，递归天然适合处理链表、树和图的相关问题，因为它们非常适合用分治思想进行分析。
    """
    # 终止条件 f(1) = 0，f(2) = 1
    if n == 1 or n == 2:
        return n - 1
    # 递归调用 f(n) = f(n - 1) + f(n - 2)
    res = fib(n - 1) + fib(n - 2)
    # 返回结果 f(n)
    return res


def for_loop_recur(n: int) -> int:
    """使用迭代模拟递归"""
    # 使用一个显式的栈模拟系统调用栈
    stack = []
    res = 0
    # 递：递归调用
    for i in range(n, 0, -1):
        # 通过“入栈操作”模拟“递”
        stack.append(i)
    # 归：返回结果
    while stack:
        # 通过“出栈操作”模拟“归”
        res += stack.pop()
    # res = 1 + 2 + ... + n
    return res


if __name__ == "__main__":
    print("recur: ", recur(10))
    print("tail_recur: ", tail_recur(10, 0))
    print("fib ", fib(10))
    print("simulation: ", for_loop_recur(10))
