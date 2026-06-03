class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force: sort the array and track all the numbers
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
            
        return longest