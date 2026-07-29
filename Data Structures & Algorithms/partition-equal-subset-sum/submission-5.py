class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        memo = [[-1] * (target + 1) for i in range(len(nums) + 1)]
        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if memo[i][target] != -1:
                return memo[i][target]
            if target < 0:
                return False
            
            memo[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])

            return memo[i][target]
        

        return dfs(0, sum(nums) // 2)