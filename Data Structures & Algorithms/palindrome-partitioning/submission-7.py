class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        
        def is_palindrome(s):
            return s == s[::-1]

        def dfs(i):
            if i == len(s):
                res.append(path[:])
                return
            
            for end in range(i + 1, len(s) + 1):
                stringg = s[i:end]

                if is_palindrome(stringg):
                    path.append(stringg)
                    dfs(end)
                    path.pop()
                else:
                    continue
        
        dfs(0)
        return res
