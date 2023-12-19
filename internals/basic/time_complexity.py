import random


def constant(n: int) -> int:
    """常数阶"""
    count = 0
    size = 100_000
    for _ in range(size):
        count += 1
    return count


def linear(n: int) -> int:
    """线性阶"""
    count = 0
    for _ in range(n):
        count += 1
    return count


def array_traversal(nums: list[int]) -> int:
    """线性阶（遍历数组）"""
    count = 0
    # 循环次数与数组长度成正比
    for num in nums:
        count += 1
    return count


def quadratic(n: int) -> int:
    """平方阶"""
    count = 0
    # 循环次数与数组长度成平方关系
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def bubble_sort(nums: list[int]) -> int:
    """平方阶（冒号排序）"""
    count = 0
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                tmp: int = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                count += 3
    return count


def exponential(n: int) -> int:
    """指数阶（循环实现）"""
    count = 0
    base = 1
    # 细胞每轮一分为二，形成数列 1, 2, 4, 8, ..., 2^(n-1)
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    # count = 1 + 2 + 4 + 8 + ... + 2^(n-1) = 2^n - 1
    return count


def exp_recur(n: int) -> int:
    """指数阶（递归实现）"""
    if n == 1:
        return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1


def logarithmic(n: float) -> int:
    """对数阶（循环实现）"""
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count


def log_recur(n: float) -> int:
    """对数阶（递归实现）"""
    if n <= 1:
        return 0
    return log_recur(n / 2) + 1


def linear_log_recur(n: float) -> int:
    """线性对数阶"""
    if n <= 1:
        return 1
    count: int = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count


def factorial_recur(n: int) -> int:
    """阶乘阶（递归实现）"""
    if n == 0:
        return 1
    count = 0
    # 从 1 个分裂出 n 个
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count


def random_numbers(n: int) -> list[int]:
    """生成一个数组，元素为：1, 2, 3, ..., n，顺序被打乱"""
    nums = [i for i in range(1, n + 1)]
    random.shuffle(nums)
    return nums


def find_one(nums: list[int]) -> int:
    """查找数组 nums 中数字 1 所在索引"""
    for i in range(len(nums)):
        if nums[i] == 1:
            return i
    return -1


if __name__ == "__main__":
    print("constant: ", constant(10))
    print("linear: ", linear(10))
    print("exponential: ", exponential(10))
