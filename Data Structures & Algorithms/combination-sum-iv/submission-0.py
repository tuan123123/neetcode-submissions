class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        1 <= nums.length <= 200 so cannot use backtracking here -> unbounded knapsack
        """
        
        memo = {}
        def dfs(target):
            if target == 0:
                return 1
            
            if target < 0:
                return 0
            
            if target in memo:
                return memo[target]
            
            
            ways = 0
            for num in nums:
                ways += dfs(target - num)
            
            memo[target] = ways
            return memo[target]
        
        return dfs(target)
                
                