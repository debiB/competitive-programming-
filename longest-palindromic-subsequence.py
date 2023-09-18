class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        max_len = 0
        def is_plain(sti):
            i,j = 0, len(sti) -1
            while i < j:
                if sti[i] != sti[j]:
                    return False
                i+=1
                j-=1
            return True
        def sub(idx, li):
            nonlocal max_len
            if idx >= len(s):
                if is_plain(li):
                    max_len = max(max_len, len(li))
                return
            li.append(s[idx])
            sub(idx+1, li)
            li.pop()
            sub(idx+1, li)
        sub(0,[])
        return max_len