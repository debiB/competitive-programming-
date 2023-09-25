class Solution:
    def bestTeamScore(self, scores: List[int], age: List[int]) -> int:
        for i in range(len(age)):
            age[i] = (age[i],scores[i])
        age.sort()
        print(age)
        dp = [1]*len(age)
        dp[len(age) - 1] = age[len(age)-1][-1]
        for j in range(len(age)-1,-1,-1):
            for k in range(j+1, len(age)):
                if age[j][-1] <= age[k][-1]:
                    dp[j] = max(dp[j], dp[k]+age[j][-1])
            if dp[j] == 1:
                dp[j] = age[j][-1]
        print(dp)
        return max(dp)