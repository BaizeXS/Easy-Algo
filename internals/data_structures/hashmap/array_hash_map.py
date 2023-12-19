"""
哈希表：
哈希冲突：
- 从本质上看，哈希函数的作用是将所有 key 构成的输入空间映射到数组所有索引构成的输出空间，输入空间往往远大于输出空间。
  因此，理论上一定存在“多个输入对应相同输出”的情况。
- 哈希表容量 n 越大，多个 key 被分配到同一个桶中的概率就越低，冲突就越少。
  因此，我们可以通过扩容哈希表来减少哈希冲突。
哈希表扩容：
- 类似于数组扩容，哈希表扩容需将所有键值对从原哈希表迁移至新哈希表，非常耗时；
  由于哈希表容量 capacity 改变，我们需要通过哈希函数来重新计算所有键值对的存储位置，这进一步提高了扩容过程的计算开销。
  为此，编程语言通常会预留足够大的哈希表容量，防止频繁扩容。
- 「负载因子 load factor」是哈希表的一个重要概念，其定义为哈希表的元素数量除以桶数量，用于衡量哈希冲突的严重程度，
  也常作为哈希表扩容的触发条件。例如在 Java 中，当负载因子超过 0.75 时，系统会将哈希表扩容至原先的 2 倍。

"""


class Pair:
    """键值对"""

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class ArrayHashMap:
    """基于数组实现的哈希表"""

    def __init__(self):
        # 初始化数组，包含100个桶
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        index = key % 100
        return index

    def get(self, key: int) -> str:
        """查询操作"""
        index: int = self.hash_func(key)
        pair: Pair | None = self.buckets[index]
        if pair is None:
            return None
        return pair.value

    def put(self, key: int, value: str):
        """添加操作"""
        pair = Pair(key, value)
        index: int = self.hash_func(key)
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
