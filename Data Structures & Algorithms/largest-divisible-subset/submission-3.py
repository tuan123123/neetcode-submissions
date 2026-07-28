class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        distinct - > no need to track duplicate postive intergers
        return subset -> list
        largest subset -> in terms of length

        1 2 3


        |
        ans


        """
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n

        last_index = 0
        maxx = 1

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                
            if dp[i] > maxx:
                maxx = dp[i]
                last_index = i
        
        ans = []
        while last_index != -1:
            ans.append(nums[last_index])
            last_index = parent[last_index]
        

        left = 0
        right = len(ans) - 1

        while left < right:
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        

        return ans
