class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for current_sum in range(target, stone - 1, -1):
                if dp[current_sum - stone]:
                    dp[current_sum] = True
        
        for subset_sum in range(target, -1, -1):
            if dp[subset_sum]:
                return total - 2 * subset_sum
