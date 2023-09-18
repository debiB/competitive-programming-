class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        str2 = s[::-1]
        li = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)-1,-1, -1):
            for j in range(len(s)-1,-1,-1):
                if s[i] == str2[j]:
                    li[i][j] = 1 + li[i+1][j+1]
                else:
                    li[i][j] = max(li[i][j+1], li[i+1][j])
        return li[0][0]