"""计数排序 Counting Sort

核心思想：通过统计元素数量来实现排序，通常应用于整数数组。

算法流程
简单实现：
给定一个长度为 n 的数组 nums，其中的元素都是“非负整数”。
1.  遍历数组，找出其中的最大数字，记为 m，然后创建一个长度为 m + 1 的辅助数组 counter。
2.  借助 counter 统计 nums 中各数字的出现次数，其中 counter[num] 对应数字 num 的出现次数。统计方法很简单，只需遍历 nums（设当前数字为
    num），每轮将 counter[num] 增加 1 即可。
3.  由于 counter 的各个索引天然有序，因此相当于所有数字已经排序好了。接下来，我们遍历 counter ，根据各数字出现次数从小到大的顺序填入 nums
    即可。

完整实现：
如果输入数据是对象，上述步骤 3 就失效了。假设输入数据是商品对象，我们想按照商品价格对商品进行排序，而上述算法只能给出价格的排序结果。为了得到
原数据的排序结果，我们需要首先计算 counter 的“前缀和”。顾名思义，索引 i 处的前缀和 prefix[i] 等于数组前 i 个元素之和：
    prefix[i] = sum_{j=0}^{i} (counter[j])
前缀和具有明确的意义，prefix[num] - 1 代表元素 num 在结果数组 res 中最后一次出现的索引。这个信息非常关键，因为它告诉我们各个元素应该出现
在结果数组的哪个位置。接下来，我们倒序遍历原数组 nums 的每个元素 num，在每轮迭代中执行以下两步。
1.  将 num 填入数组 res 的索引 prefix[num] - 1 处。
2.  令前缀和 prefix[num] 减小 1，从而得到下次放置 num 的索引。
遍历完成后，数组 res 中就是排序好的结果，最后使用 res 覆盖原数组 nums 即可。

算法特性：
时间复杂度：O(n+m)，涉及遍历 nums 和 counter，都是线性时间。
空间复杂度：O(n+m)，借助长度为 n 和 m 的数组 res 和 counter。
非原地排序
稳定排序：由于向 res 中填充元素的顺序是“从右向左”的，因此倒序遍历 nums 可以避免改变相等元素之间的相对位置，从而实现稳定排序。实际上，正序
         遍历 nums 也可以得到正确的排序结果，但结果是非稳定的。

局限性：
- 计数排序只适用于非负整数。
- 计数排序适合数据量大但是数据范围小的情况。
"""


def counting_sort_naive(nums: list[int]):
    """计数排序"""
    # 简单实现，无法用于排序对象
    # 1. 统计数组最大元素 m
    m = 0
    for num in nums:
        m = max(m, num)
    # 2. 统计各数数字出现的次数
    counter = [0] * (m + 1)
    for num in nums:
        counter[num] += 1
    # 3. 遍历 counter，将各元素填入原数组 nums
    i = 0
    for num in range(m+1):
        for _ in range(counter[num]):
            nums[i] = num
            i += 1


def counting_sort(nums: list[int]):
    """计数排序"""
    # 完整实现，可排序对象，并且稳定排序
    # 1. 统计数组最大元素 m
    m = max(nums)
    # 2. 统计各数数字出现的次数
    counter = [0] * (m + 1)
    for num in nums:
        counter[num] += 1
    # 3. 求 counter 的前缀和，将“出现次数”转化为“尾索引”
    for i in range(m):
        counter[i + 1] += counter[i]
    # 4. 倒序遍历 nums，将各元素填入结果数组 res
    n = len(nums)
    res = [0] * n
    for i in range(n - 1, -1, -1):
        num = nums[i]
        res[counter[num] - 1] = num  # 将 num 放置到对应索引处
        counter[num] -= 1  # 令前缀和自减 1，得到下次放置 num 的索引
    for i in range(n):
        nums[i] = res[i]
