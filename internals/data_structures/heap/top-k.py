"""
Question: 给定一个长度为 n 的无序数组 nums，请返回数组中前 k 大的元素

流程
1. 初始化一个小顶堆，其堆顶元素最小。
2. 先将数组的前 k 个元素依次入堆。
3. 从第 k+1 个元素开始，若当前元素大于堆顶元素，则将堆顶元素出堆，并将当前元素入堆。
4. 遍历完成后，堆中保存的就是最大的 k 个元素。

总共执行了 n 轮入堆和出堆，堆的最大长度为 k，因此时间复杂度为 O(n log k)。该方法的效率很高，
当 k 较小时，时间复杂度趋向 O(n)；当 k 较大时，时间复杂度不会超过 O(n log n)。

另外，该方法适用于动态数据流的使用场景。在不断加入数据时，我们可以持续维护堆内的元素，从而实现
最大 k 个元素的动态更新。
"""
import heapq


def top_k(nums, k):
    """基于堆查找数组中最大的 k 个元素"""
    # 初始化小顶堆
    top_k_heap = []
    # 将数组的前 k 个元素入堆
    for i in range(k):
        heapq.heappush(top_k_heap, nums[i])
    # 从 k+1 个元素开始，保持堆的长度为 k
    for i in range(k, len(nums)):
        if nums[i] > top_k_heap[0]:
            heapq.heappop(top_k_heap)
            heapq.heappush(top_k_heap, nums[i])
    return top_k_heap

