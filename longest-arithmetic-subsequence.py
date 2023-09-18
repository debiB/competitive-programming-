class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda:1)
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i, diff] = 1 + dp[j,diff]
        return max(dp.values())