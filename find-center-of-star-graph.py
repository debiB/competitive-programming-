from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        for k in d.keys():
            if len(d[k]) == len(d) - 1:
                return k