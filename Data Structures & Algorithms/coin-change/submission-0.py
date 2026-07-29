class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def dfs(amount1):
            if amount1 in memo:
                return memo[amount1]
            
            minn = float('inf')
            for coin in coins:
                diff = amount1 - coin
                if diff < 0:
                    break
                
                minn = min(minn, 1 + dfs(diff))
            
            memo[amount1] = minn
            return memo[amount1]
        

        result = dfs(amount)

        if result < float('inf'):
            return result
        else:
            return -1