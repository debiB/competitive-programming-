class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    
        adj_list = defaultdict(list)
        for u, v in adjacentPairs:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        
        start = None
        for node, neighbors in adj_list.items():
            if len(neighbors) == 1:
                start = node
                break
        
    
        visited = set()
        q = deque([start])
        result = []
        
        while q:
            node = q.popleft()
            visited.add(node)
            result.append(node)
            
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    q.append(neighbor)
        
        return result