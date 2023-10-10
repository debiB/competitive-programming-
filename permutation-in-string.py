class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def helper(a,b):
            for i in range(len(a)):
                if(a[i] != b[i]):
                    return False
            return True
        freq1 = [0]*26
        freq2 = [0]*26
        for i in range(len(s1)):
            freq1[ord(s1[i]) -97]+=1
            j=0
        for i in range(len(s2)):
            freq2[ord(s2[i]) -97]+=1
            if(i-j+1 >= len(s1)):
                if helper(freq1, freq2):
                    return True
                else:
                   freq2[ord(s2[j]) - 97]-=1 
                   j+=1
        return False