class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def dfs(start_index, path):
            ans.append(path[:])
            
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

            
        dfs(0, [])
        return ans