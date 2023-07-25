class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0 
        def backtrack(idx, bitmask):
            nonlocal ans
            if idx == n:
                ans+=1 
                return 
            for i in range(1,n+1):
                if (bitmask & (1<<i)) == 0 and ((idx+1)% i == 0 or i %(idx+1) == 0):
                    bitmask |= (1<<i)
                    backtrack(idx+1,bitmask)
                    bitmask &= ~(1<<i)
        backtrack(0,0)
        return ans