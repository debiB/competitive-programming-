from collections import defaultdict
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        visited = set()
        def dfs(root):
            visited.add(root)
            counter = 0
            for ch in d[root]:
                if ch in visited:
                    continue
                ctime = dfs(ch)
                counter += ctime + 2 if hasApple[ch] or ctime > 0 else 0
            return counter
        
        return dfs(0)