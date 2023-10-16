class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        li = [True]*(n+1)
        li[0], li[1] = False, False
        for i in range(2, round(n**0.5)+1):
            if li[i]:
                for j in range(i*i,n, i):
                    li[j] = False
        return li.count(True)-1