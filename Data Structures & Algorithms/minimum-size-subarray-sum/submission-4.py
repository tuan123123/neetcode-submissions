class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        prefix sum
        

        2 1 5 1 5 3
              l
                   r
        min = 4

        """
        prefix = [0] * (len(nums) + 1)
        prefix[1] = nums[0]
        for i in range(2, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        l, r = 1, 1
        minn = float('inf')
        while r <= len(nums):
            summ = prefix[r] - prefix[l - 1]
            if summ < target:
                r += 1
            elif summ >= target:
                minn = min(r - l + 1, minn)
                l += 1
                

        if minn == float('inf'):
            return 0
        else:
            return minn

