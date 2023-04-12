from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) <= 1:
            return True
        d = defaultdict(list)
        for i in dislikes:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        li = [-1]*(n+1)
        def helper(node, color):
            li[node] = color
            for i in d[node]:
                if li[i] == 1-color:
                    continue
                elif li[i] == color:
                    return False
                if not helper(i, 1-color):
                    return False
            return True 
        for k in d.keys():
            if li[k] != -1:
                continue
            if not helper(k,0):
                return False
        return True