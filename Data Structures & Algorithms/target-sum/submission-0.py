class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, target1):
            if i == len(nums) and target1 == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            if (i, target1) in memo:
                return memo[(i, target1)]
            
            positive = dfs(i + 1, target1 + nums[i])
            negative = dfs(i + 1, target1 + -nums[i])
            memo[(i, target1)] = positive + negative

            return memo[(i, target1)]
        
        return dfs(0, 0)