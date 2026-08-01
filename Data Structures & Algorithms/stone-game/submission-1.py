class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            alice_turn = (r - l + 1) % 2 == 0

            left = piles[l] if alice_turn else 0
            right = piles[r] if alice_turn else 0

            take_left = left + dfs(l + 1, r)
            take_right = right + dfs(l, r - 1)

            if alice_turn:
                dp[(l, r)] = max(take_left, take_right)
            else:
                dp[(l, r)] = min(take_left, take_right)

            return dp[(l, r)]

        total = sum(piles)
        alice = dfs(0, len(piles) - 1)

        return alice > total - alice