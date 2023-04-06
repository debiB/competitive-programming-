class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        d=2 
        while(n>1):
            while(n%d == 0):
                res+=d
                n//=d
            d+=1
        return res
