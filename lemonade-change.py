class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = defaultdict(int)
        for i in bills:
            if i == 5:
               d[i]+=1
            if i == 10:
                if d[5] == 0:
                    return False
                else:
                    d[5]-=1
                d[10]+=1
            if i == 20:
                if d[5] == 0:
                    return False

                elif d[10] >= 1 and d[5] >= 1:
                    d[5]-=1
                    d[10]-=1
                elif d[5] >= 3:
                    d[5]-=3
                else:
                    return False
        return True