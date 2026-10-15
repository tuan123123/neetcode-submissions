class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i in dp:
                return dp[i]
            
            first = dfs(i + 1)
            second = dfs(i + 2)

            dp[i] = cost[i] + min(first, second)

            return dp[i]
        
        return min(dfs(0), dfs(1))
