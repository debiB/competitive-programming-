class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            ans = helper(x, n//2)
            if n%2 == 0:
                return ans*ans
            else:
                return ans*ans*x
        flag = True 
        if n < 0:
            flag = False
        if flag:
           return helper(x,n)
        else:
            return 1/helper(x,-n)