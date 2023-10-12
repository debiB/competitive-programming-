class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        res = length
        j = 0 
        for i in range(len(nums)):
            while j < len(nums) and nums[j] < nums[i] + length:
               j+=1
            window = j-i
            res = min(res, length- window)
        return res