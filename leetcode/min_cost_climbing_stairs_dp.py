class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        if n == 0 or n == 1:
            return 0

        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])

    def minCostClimbingStairs2(self, cost: list[int]) -> int:
        n = len(cost)
        if n == 0 or n == 1:
            return 0

        a, b = cost[0], cost[1]

        for i in range(2, n):
            a, b = b, cost[i] + min(a, b)

        return min(a, b)
