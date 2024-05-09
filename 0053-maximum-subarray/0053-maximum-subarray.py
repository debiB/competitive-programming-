class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        for i in range(len(nums)):
            if i-1 < 0:
                prev= 0 
            else:
                prev = dp[i-1]       
            dp[i] = max(nums[i] + prev, nums[i])
       
        return max(dp)
        