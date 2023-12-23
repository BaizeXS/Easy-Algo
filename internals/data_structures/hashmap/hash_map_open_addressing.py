"""
开放寻址哈希表

1. 「开放寻址 open addressing」不引入额外的数据结构，而是通过“多次探测”来处理哈希冲突，
   探测方式主要包括线性探测、平方探测、多次哈希等。
2. 线性探测
    a. 线性探测采用固定步长的线性搜索来进行探测，其操作方法与普通哈希表有所不同。
        - 插入元素：通过哈希函数计算桶索引，若发现桶内已有元素，则从冲突位置向后线性遍历（步长通常为 1），
            直至找到空桶，将元素插入其中。
        - 查找元素：若发现哈希冲突，则使用相同步长向后线性遍历，直到找到对应元素，返回 value 即可；
            如果遇到空桶，说明目标元素不在哈希表中，返回 None。
    b. 线性探测容易产生“聚集现象”。
        具体来说，数组中连续被占用的位置越长，这些连续位置发生哈希冲突的可能性越大，从而进一步促使该位置的聚堆生长，
        形成恶性循环，最终导致增删查改操作效率劣化。
    c. 不能在开放寻址哈希表中直接删除元素。
        这是因为删除元素会在数组内产生一个空桶 None，而当查询元素时，线性探测到该空桶就会返回，因此在该空桶之下的元
        素都无法再被访问到，程序可能误判这些元素不存在。
    d. 可以采用「懒删除 lazy deletion」机制应对 `c` 中提到的问题。
        - 它不直接从哈希表中移除元素，而是利用一个常量 TOMBSTONE 来标记这个桶。在该机制下，None 和 TOMBSTONE 都代表空桶，
          都可以放置键值对。但不同的是，线性探测到 TOMBSTONE 时应该继续遍历，因为其之下可能还存在键值对。
        - 懒删除可能会加速哈希表的性能退化。这是因为每次删除操作都会产生一个删除标记，随着 TOMBSTONE 的增加，搜索时间也会
          增加，因为线性探测可能需要跳过多个 TOMBSTONE 才能找到目标元素。
        - 在线性探测中记录遇到的首个 TOMBSTONE 的索引，并将搜索到的目标元素与该 TOMBSTONE 交换位置。
          这样做的好处是当每次查询或添加元素时，元素会被移动至距离理想位置（探测起始点）更近的桶，从而优化查询效率。
3. 平方探测
    a. 当发生冲突时，平方探测不是简单地跳过一个固定的步数，而是跳过“探测次数的平方”的步数，即1，4，9，... 步。
    b. 平方探测的主要优势
        - 平方探测通过跳过探测次数平方的距离，试图缓解线性探测的聚集效应。
        - 平方探测会跳过更大的距离来寻找空位置，有助于数据分布得更加均匀。
    c. 平方探测的主要劣势
        - 存在聚集现象。
        - 由于平方的增长，平方探测可能不会探测整个哈希表，这意味着即使哈希表中有空桶，平方探测也可能无法访问到它。
4. 多次哈希
    多次哈希方法使用多个哈希函数 f1(x)、f2(x)、f3(x)、... 进行探测。
        - 插入元素：若哈希函数 f1(x) 出现冲突，则尝试 f2(x)，以此类推，直到找到空桶后插入元素。
        - 查找元素：在相同的哈希函数顺序下进行查找，直到找到目标元素时返回；
          若遇到空桶或已尝试所有哈希函数，说明哈希表中不存在该元素，则返回 None。
        - 与线性探测相比，多次哈希方法不易产生聚集，但多个哈希函数会带来额外的计算量。
5. 请注意，开放寻址（线性探测、平方探测和多次哈希）哈希表都存在“不能直接删除元素”的问题。
6. 编程语言的选择：
    - Python 采用开放寻址。字典 dict 使用伪随机数进行探测。
    - Java 采用链式地址。自 JDK 1.8 以来，当 HashMap 内数组长度达到 64 且链表长度达到 8 时，
      链表会转换为红黑树以提升查找性能。
    - Go 采用链式地址。Go 规定每个桶最多存储 8 个键值对，超出容量则连接一个溢出桶。
      当溢出桶过多时，会执行一次特殊的等量扩容操作，以确保性能。
"""

from __future__ import annotations

from internals.data_structures.hashmap.hash_map import Pair


class HashMapOpenAddressing:

    def __init__(self):
        """构造方法"""
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_threshold = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets: list[Pair | None] = [None] * self.capacity  # 桶数组
        self.TOMBSTONE = Pair(-1, "-1")  # 删除标记

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        return key % self.capacity

    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capacity

    def find_bucket(self, key: int) -> int:
        """搜索 key 对应的桶索引"""
        index = self.hash_func(key)
        first_tombstone = -1
        # 线性探测
        while self.buckets[index] is not None:
            # 若遇到 key，则返回桶索引
            if self.buckets[index].key == key:
                # 若遇到了删除标记，怎讲键值对移动到该索引
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tombstone
                return index
            # 记录遇到的首个删除标记
            if self.buckets[index] is self.TOMBSTONE and first_tombstone == -1:
                first_tombstone = index
            # 计算桶索引，越过尾部则返回头部
            index = (index + 1) % self.capacity
        return index if first_tombstone == -1 else first_tombstone

    def extend(self):
        """扩展哈希表"""
        buckets_temp = self.buckets

        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0

        for pair in buckets_temp:
            if pair not in [None, self.TOMBSTONE]:
                self.put(pair.key, pair.value)

    def get(self, key: int) -> str | None:
        """查询元素"""
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            return self.buckets[index].value
        return None

    def put(self, key: int, value: str):
        """添加操作"""
        if self.load_factor() > self.load_threshold:
            self.extend()
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index].value = value
            return
        self.buckets[index] = Pair(key, value)
        self.size += 1

    def remove(self, key: int):
        """删除操作"""
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1

    def print(self):
        """打印哈希表"""
        for pair in self.buckets:
            if pair is None:
                print("None")
            elif pair is self.TOMBSTONE:
                print("TOMBSTONE")
            else:
                print(pair.key, "->", pair.val)

