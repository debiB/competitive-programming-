from typing import List

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V

        for v in range(V):
            if not visited[v] and self.isCycleUtil(v, adj, visited, -1):
                return True
        
        return False

    def isCycleUtil(self, v: int, adj: List[List[int]], visited: List[bool], parent: int) -> bool:
        visited[v] = True

        for neighbor in adj[v]:
            if not visited[neighbor]:
                if self.isCycleUtil(neighbor, adj, visited, v):
                    return True
            elif neighbor != parent:
                return True
        
        return False
