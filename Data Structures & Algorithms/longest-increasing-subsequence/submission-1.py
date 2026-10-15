class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            longest = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    longest = max(longest, 1 + dfs(j))
            
            memo[i] = longest
            return memo[i]
        
        maxx = 1
        for i in range(len(nums)):
            maxx = max(maxx, dfs(i))
        
        return maxx