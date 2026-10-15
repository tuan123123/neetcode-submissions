class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo = {}

        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     longest = 1
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] > nums[i]:
        #             longest = max(longest, 1 + dfs(j))
            
        #     memo[i] = longest
        #     return memo[i]
        
        # maxx = 1
        # for i in range(len(nums)):
        #     maxx = max(maxx, dfs(i))
        
        # return maxx
    
        # """
        # O(n^2)
        # O(n)
        # """

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)