class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i  >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            skip = dfs(i + 1)
            take = nums[i] + dfs(i + 2)
            memo[i] =  max(skip, take)
            return max(skip, take)

        
        return dfs(0)

