class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        def dfs(i, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for j in range(i, len(nums)):
                num = nums[j]

                if num <= remaining:
                    path.append(num)
                    dfs(j, remaining - num)
                    path.pop()
        
        dfs(0, target)

        return res
                    