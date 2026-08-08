class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        prefix sum
        

        2 1 5 1 5 3
              l
                   r
        min = 4

        """
        l, total = 0, 0
        minn = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minn = min(r - l + 1, minn)
                total -= nums[l]
                l += 1
                
        
        return 0 if minn == float('inf') else minn

