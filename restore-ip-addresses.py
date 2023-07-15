class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans =[]
        if len(s) > 12:
            return ans
        def backtrack(dots,cur,idx):
            nonlocal ans
            if idx >= len(s) and dots == 4:
                ans.append(cur[:-1])
                return 
            if dots > 4:
                return 
            for i in range(idx, min((idx+3), len(s))):
                if int(s[idx:i+1]) < 256 and (i==idx or s[idx] != '0'):

                    backtrack(dots+1, cur +s[idx:i+1] + ".", i+1)
        backtrack(0, "", 0)
        return ans