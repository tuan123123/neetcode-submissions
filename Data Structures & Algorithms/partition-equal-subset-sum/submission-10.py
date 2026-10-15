class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        n = len(nums)
        dp = {}
        total = sum(nums)
        target = total // 2
        def dfs(i, summ):
            if summ == 0:
                return True
            if i >= n or summ < 0:
                return False
            if (i, summ) in dp:
                return dp[(i, summ)]

            skip = dfs(i + 1, summ)

            
            take = dfs(i + 1, summ - nums[i])
            
            dp[(i, summ)] = skip or take

            return dp[(i, summ)]
        
        return dfs(0, target)
            
