from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)
        visited = set()
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        def helper(node):
            if node == destination:
                return True
            visited.add(node)
            for i in d[node]:
                if i not in visited and helper(i):
                    return True
            return False
        return helper(source)