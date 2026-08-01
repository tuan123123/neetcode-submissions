class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            skip = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, buying)] = max(buy, skip)
            else:
                # After selling, skip the next day.
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, buying)] = max(sell, skip)

            return dp[(i, buying)]

        return dfs(0, True)