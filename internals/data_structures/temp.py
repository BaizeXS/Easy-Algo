import heapq


class Solution:
    def smallestK(self, arr: list[int], k: int) -> list[int]:
        return heapq.nsmallest(k, arr)
