class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return res
