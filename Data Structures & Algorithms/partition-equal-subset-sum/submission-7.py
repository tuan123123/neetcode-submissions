class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        memo = {}
        def dfs(i, remaining):
            if remaining == 0:
                return True
            
            if i == len(nums) or remaining < 0:
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            skip = dfs(i + 1, remaining)
            take = dfs(i + 1, remaining - nums[i])
            memo[(i, remaining)] = skip or take
            return memo[(i, remaining)]
        
        return dfs(0, sum(nums) // 2)