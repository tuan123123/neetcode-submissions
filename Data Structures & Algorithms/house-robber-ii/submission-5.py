class Solution:
    def rob(self, nums: List[int]) -> int:
        if len == 1:
            return nums[0]
        
        def dfs(house):

            rob1 ,rob2 = 0, 0

            for num in house:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        
        return max(dfs(nums[:-1]), dfs(nums[1:]), nums[0])
        