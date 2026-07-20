class Solution:

    def help(self, nums):
        if len(nums) == 1:
            return nums[0]

        house0, house1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(nums[i] + house0, house1)
            house0, house1 = house1, curr
        
        return house1
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.help(nums[1:]), self.help(nums[:-1]))