class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target_hash = 0
        for i in s1:
            c = ord(i) - 96
            target_hash += (c ** 4)
        hash_val = 0
        for i in range(len(s1)):
            c = ord(s2[i]) - 96
            hash_val += (c ** 4)
        if target_hash == hash_val:
            return True
        
        k, j = 0, len(s1)
        while j < len(s2):
            dec = ord(s2[k]) - 96
            add = ord(s2[j]) - 96
            hash_val -= (dec ** 4)
            hash_val += (add ** 4)
            if hash_val == target_hash:
                return True
            k += 1
            j += 1
            
        return False