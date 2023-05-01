class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = ""
        i, j = 0, 0
        
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                ans += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                ans += word2[j]
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    ans += word1[i]
                    i += 1
                else:
                    ans += word2[j]
                    j += 1
        
        ans += word1[i:]
        ans += word2[j:]
        
        return ans