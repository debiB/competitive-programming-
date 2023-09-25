class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(2,n+1):
            total = 0
            for j in range(1,i+1):
                total += dp[i-j] * dp[j-1]
            dp[i] = total
        return dp[n]