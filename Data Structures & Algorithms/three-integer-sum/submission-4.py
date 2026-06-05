class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            res = []
            nums.sort()
            for i, c in enumerate(nums):
                if c > 0:
                    break
                
                if i > 0 and c == nums[i - 1]:
                    continue
                
                l, r = i + 1, len(nums) - 1
                while l < r:
                    threeSum = c + nums[l] + nums[r]
                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        res.append([c, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        
            return res