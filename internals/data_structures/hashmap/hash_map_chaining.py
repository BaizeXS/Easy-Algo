"""
链式地址哈希表
1. 在原始哈希表中，每个桶仅能存储一个键值对。「链式地址 separate chaining」将单个元素转换为链表，
   将键值对作为链表节点，将所有发生冲突的键值对都存储在同一链表中。
2. 基于链式地址实现的哈希表的操作方法发生了以下变化
    - 查询元素：输入 key，经过哈希函数得到桶索引，即可访问链表头节点，然后遍历链表并对比 key 以查找目标键值对。
    - 添加元素：首先通过哈希函数访问链表头节点，然后将节点（键值对）添加到链表中。
    - 删除元素：根据哈希函数的结果访问链表头部，接着遍历链表以查找目标节点并将其删除。
3. 链式地址存在以下局限性
    - 占用空间增大，链表包含节点指针，它相比数组更加耗费内存空间。
    - 查询效率降低，因为需要线性遍历链表来查找对应元素。
4. 值得注意的是，当链表很长时，查询效率 O(n) 很差。
   此时可以将链表转换为“AVL 树”或“红黑树”，从而将查询操作的时间复杂度优化至 O(log n)。
"""
from __future__ import annotations

from internals.data_structures.hashmap.hash_map import Pair


class HashMapChaining:

    def __init__(self):
        """构造方法"""
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_threshold = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]  # 桶数据

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        return key % self.capacity

    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capacity

    def extend(self):
        """扩容哈希表"""
        # 暂存哈希表
        buckets = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        # 将键值对从原来的哈希表搬运到新的哈希表
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.value)

    def get(self, key: int) -> str | None:
        """查询操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，若找到 key 则返回对应的 value
        for pair in bucket:
            if pair.key == key:
                return pair.value
        # 若未找到 key 则返回 None
        return None

    def put(self, key: int, value: str):
        """添加操作"""
        # 负载因子超过阈值时，执行扩容操作
        if self.load_factor() > self.load_threshold:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，若遇到指定 key ，则更新对应 val 并返回
        for pair in bucket:
            if pair.key == key:
                pair.value = value
                return
        # 若无该 key 则将键值对添加至尾部
        pair = Pair(key, value)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        """删除操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def print(self):
        """打印哈希表"""
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + " -> " + str(pair.value))
            print(res)
