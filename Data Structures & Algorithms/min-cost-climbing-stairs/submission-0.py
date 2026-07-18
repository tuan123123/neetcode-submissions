class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            first = dfs(i + 1)
            second = dfs(i + 2)
            memo[i] = cost[i] + min(first, second)
            return cost[i] + min(first, second)
        
        return min(dfs(0), dfs(1))