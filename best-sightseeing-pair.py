class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        _max = 0
        dp = [0]*len(values)

        for i in range(1,len(values)):
                dp[i] = max(dp[i-1], values[i-1]+ i-1)
                _max = max(_max, dp[i]+ values[i] -i)
        return _max