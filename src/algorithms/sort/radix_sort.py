"""基数排序 Radix Sort

核心思想：
基数排序核心思想与计数排序一致，也通过统计个数来实现排序。在此基础上，基数排序利用数字各位之间的递进关系，依次对每一位进行排序，从而得到最终的
排序结果。


算法流程：
以8位数字的学号数据为例，假设数字的最低位是第 1 位，最高位是第 8 位。
1.  初始化位数 k = 1
2.  对学号的第 k 位执行“计数排序”。完成后数据会根据第 k 位从小到大排序。
3.  将 k 增加 1，然后返回步骤 2 继续迭代，直到所有位都排序完成后结束。

剖析代码实现
对于一个 d 进制的数字 x，要获取其第 k 位 x_{k}，可以使用以下计算公式：
    x_{k} = ⌊ x / {d^{k-1} ⌋ mod d
其中 ⌊a⌋ 表示对浮点数 a 向下取整，而 mod d 表示对 d 取模。对于学号数据，d = 10 且 k 属于 [1, 8]

算法特性
相较于计数排序，基数排序适用于数值范围较大的情况，但是**前提是数据必须可以表示为固定位数的格式，且位数不能过大**。例如浮点数不适合使用基数排序，
因为位数 k 过大，可能导致时间复杂度 O(nk) >> O(n^2)。
时间复杂度：O(nk)
空间复杂度：O(n+d)
非原地排序
稳定排序：当计数排序稳定时，基数排序也稳定；当计数排序不稳定时，基数排序无法保证得到正确的排序结果。
"""


def digit(num: int, exp: int) -> int:
    """获取元素 num 的第 k 位，其中 exp = 10 ^ (k - 1)"""
    # 传入 exp 而非 k 可以避免在此重复执行昂贵的次方计算
    return (num // exp) % 10


def counting_sort_digit(nums: list[int], exp: int):
    """计数排序（根据 nums 第 k 位排序）"""
    # 十进制的范围为 0～9，因此需要长度为 10 的桶数组
    counter = [0] * 10
    n = len(nums)
    # 统计 0～9 各自出现的次数
    for i in range(n):
        d = digit(nums[i], exp)
        counter[d] += 1
    # 求前缀和，将“出现个数”转换为“数组索引”
    for i in range(1, 10):
        counter[i] += counter[i - 1]
    # 倒序遍历，根据桶内统计结果，将各元素填入 res
    res = [0] * n
    for i in range(n - 1, -1, -1):
        d = digit(nums[i], exp)
        j = counter[d] - 1
        res[j] = nums[i]
        counter[d] -= 1
    # 使用结果覆盖原数组 nums
    for i in range(n):
        nums[i] = res[i]


def radix_sort(nums: list[int]):
    """基数排序"""
    # 获取数组的最大元素，用于判断最大位数
    m = max(nums)
    # 按照从低位到高位的顺序遍历
    exp = 1
    while exp < m:
        counting_sort_digit(nums, exp)
        exp *= 10
