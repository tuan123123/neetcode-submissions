class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            for j in range(i, len(s)):
                if s[i : j  + 1] in wordSet:
                    if dfs(j + 1):
                        dp[j + 1] = True
                        return True
            dp[i] = False
            return False
        
        return dfs(0)