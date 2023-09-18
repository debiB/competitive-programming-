class Solution:
    def minSteps(self, n: int) -> int:
        dp = {}
        dp[1], dp[2] = 0,2
        for i in range(3,n+1):
            dp[i] = i 
            j = 2
            while(j < round(i**0.5)+1):
                if(i%j == 0):
                    dp[i] = min(dp[i], dp[i/j]+j)
                j+=1
        return dp[n]