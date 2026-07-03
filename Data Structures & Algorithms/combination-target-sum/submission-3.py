class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(nums, index, path, summ):
            if summ == 0:
                result.append(path[:])
                return
            

            for i in range(index, len(nums)):
                num  = nums[i]
                if summ - num < 0:
                    break
                
                path.append(num)
                dfs(nums, i, path, summ - num)
                path.pop()
            
        nums.sort()
        dfs(nums, 0, [], target)
        return result