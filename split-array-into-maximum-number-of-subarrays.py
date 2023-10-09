class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        min_ele= nums[0]
        n = 2**32-1
        score = 0
        for i in range(len(nums)):
            n&= nums[i]
            if n == 0:
                n = 2**32-1 
                score+=1
            #n&= nums[i]
        return score if score != 0 else 1