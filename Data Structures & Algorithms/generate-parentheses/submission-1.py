class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(start_index, opencounts, closecounts):
            if start_index == 2 * n:
                res.append("".join(path[:]))
                return
            
            if opencounts < n:
                path.append("(")
                dfs(start_index + 1, opencounts + 1, closecounts)
                path.pop()
            
            if opencounts > closecounts:
                path.append(")")
                dfs(start_index + 1, opencounts, closecounts + 1)
                path.pop()
            
        
        dfs(0, 0 ,0)
        return res
