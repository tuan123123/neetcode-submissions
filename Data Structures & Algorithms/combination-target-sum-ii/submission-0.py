class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, sol = [], []
        candidates.sort()
        def dfs(start_index, path, remaining):
            if remaining == 0:
                ans.append(path[:])
                return
            
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                dfs(i + 1, path, remaining - candidates[i])
                path.pop()
            

        
        dfs(0, [], target)
        return ans
            
