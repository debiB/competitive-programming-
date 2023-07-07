from collections import defaultdict
from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))
        
        def find(root):
            if root != parent[root]:
                parent[root] = find(parent[root])
            return parent[root]
        
        def union(root1, root2):
            parent[find(root1)] = find(root2)
        
        for i, j in pairs:
            union(i, j)
        
        igrp = defaultdict(list)
        cgrp = defaultdict(list)
        
        for i in range(len(s)):
            c=find(i) 
            igrp[c].append(i)
            cgrp[c].append(s[i])
        
        res = [""] * len(s)
        
        for group in igrp.keys():
            idx = sorted(igrp[group])
            char = sorted(cgrp[group])
            for i, c in zip(idx, char):
                res[i] = c
        
        return "".join(res)