"""
哈希表

* 注：考虑最简单的情况，仅用一个数组来实现哈希表。

1. 在哈希表中，我们将数组中的每个空位称为「桶 bucket」，每个桶可存储一个键值对。
2. 查询操作就是找到 key 对应的桶，并在桶中获取 value。
3. 借助「哈希函数 hash function」，我们可以基于 key 定位到对应的桶。


哈希函数：

1. 哈希函数的作用是将一个较大的输入空间映射到一个较小的输出空间。在哈希表中，输入空间是所有 key，输出空间是所有桶（数组索引）。
2. 通过哈希函数得到该 key 对应的键值对在数组中的存储位置：
    a. 通过某种哈希算法 hash() 计算得到哈希值。
    b. 将哈希值对桶数量 capacity 取模，从而获取该 key 对应的数组索引 index


哈希冲突：

1. 从本质上看，哈希函数的作用是将所有 key 构成的输入空间映射到数组所有索引构成的输出空间，输入空间往往远大于输出空间。
   因此，理论上一定存在“多个输入对应相同输出”的情况。
2. 哈希表容量 n 越大，多个 key 被分配到同一个桶中的概率就越低，冲突就越少。因此，我们可以通过扩容哈希表来减少哈希冲突。
3. 通常情况下哈希函数的输入空间远大于输出空间，因此理论上哈希冲突是不可避免的。
4. 哈希冲突会导致查询结果错误，严重影响哈希表的可用性。
5. 为解决该问题，我们可以每当遇到哈希冲突就进行哈希表扩容，直至冲突消失为止。此方法简单粗暴且有效，但效率太低，
   因为哈希表扩容需要进行大量的数据搬运与哈希值计算。
6. 为了提升效率，我们可以采用以下策略：
    a. 改良哈希表数据结构，使得哈希表可以在出现哈希冲突时正常工作。
    b. 仅在必要时，即当哈希冲突比较严重时，才执行扩容操作。
7. 哈希表的结构改良方法主要包括「链式地址」和「开放寻址」。


哈希表扩容

1. 类似于数组扩容，哈希表扩容需将所有键值对从原哈希表迁移至新哈希表，非常耗时；
2. 由于哈希表容量 capacity 改变，我们需要通过哈希函数来重新计算所有键值对的存储位置，这进一步提高了扩容过程的计算开销。
3. 因此，编程语言通常会预留足够大的哈希表容量，防止频繁扩容。
4.「负载因子 load factor」是哈希表的一个重要概念，其定义为哈希表的元素数量除以桶数量，用于衡量哈希冲突的严重程度，
  也常作为哈希表扩容的触发条件。例如在 Java 中，当负载因子超过 0.75 时，系统会将哈希表扩容至原先的 2 倍。
"""
from __future__ import annotations


class Pair:
    """键值对"""

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class ArrayHashMap:
    """基于数组实现的哈希表"""

    def __init__(self, capacity: int = 100):
        # 初始化数组，包含100个桶
        self.capacity = capacity
        self.buckets: list[Pair | None] = [None] * self.capacity

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        index = key % self.capacity
        return index

    def get(self, key: int) -> str | None:
        """查询操作"""
        index = self.hash_func(key)
        pair = self.buckets[index]
        if pair is None:
            return None
        return pair.value

    def put(self, key: int, value: str):
        """添加操作"""
        pair = Pair(key, value)
        index = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int):
        """删除操作"""
        index: int = self.hash_func(key)
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        """获取所有键值对"""
        result: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result

    def key_set(self) -> list[int]:
        """获取所有键"""
        result: list[int] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def value_set(self) -> list[str]:
        """获取所有值"""
        result: list[str] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.value)
        return result

    def print(self):
        """打印哈希表"""
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.value)
