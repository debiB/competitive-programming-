class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = "aeiou"
        dp = [0]*n
        if word[0] in vowels:
            dp[0]= 1
        for i in range(1,n):
            if word[i] in vowels:
                dp[i]=dp[i-1] + i +1
            else: 
                dp[i] = dp[i-1]
    
        return sum(dp)