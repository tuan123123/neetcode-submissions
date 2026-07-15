class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        vote = 0

        for num in nums:
            if vote == 0:
                candidate = num
            
            vote += (1 if num == candidate else -1)
        
        return candidate

