class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        sol = []

        used = [False] * len(nums)

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):

                if used[i]:
                    continue
                
                if(i > 0  and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                
                used[i] = True
                sol.append(nums[i])
                backtrack()
                sol.pop()
                used[i] = False
        
        backtrack()
        return res
                