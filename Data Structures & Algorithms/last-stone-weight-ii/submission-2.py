class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = 0
        for stone in stones:
            summ += stone

        target = (summ + 1) // 2

        memo = {}

        def dfs(i, total):
            if i >= len(stones) or total == target:
                return abs(total - (summ -total))

            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))

            return memo[(i, total)]

        return dfs(0, 0)

        """
        divide into two groups whose sums are as close as possible

        0/1 knapsack

        """
