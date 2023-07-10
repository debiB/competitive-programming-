from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        d = defaultdict(list)
    
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        
        leaves = []
        for k in d.keys():
            if len(d[k]) == 1:
                leaves.append(k) 

        while n > 2:
            n_leaves = []
            for leave in leaves:
                nq = d[leave].pop()
                d[nq].remove(leave)
                if len(d[nq]) == 1:
                    n_leaves.append(nq)
                n-=1
            leaves = n_leaves
        return leaves