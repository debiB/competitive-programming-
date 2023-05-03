class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        def inbound(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]):
                return True
            return False
        visited = set()
        def dfs(i,j):
            if not inbound(i,j) or (i,j) in visited or grid[i][j] == 0:
                return 
            visited.add((i,j))
            for a,b in directions:
                if inbound(i+a, j+b) and (i+a, j+b) not in visited:
                    dfs(i+a, j+b)
        def bfs():
            q = deque(visited)
            counter = -1
            visit = set(visited)
            while q:
                counter+=1
                l = len(q)
                for _ in range(len(q)):
                    c,d= q.popleft()
                    for a,b in directions:
                        if inbound(c+a,d+b) and (c+a, d+b) not in visit and grid[c+a][d+b] == 1:
                            return counter
                        if inbound(a+c, b+d) and (c+a, d+b) not in visit and grid[c+a][d+b] == 0:
                            visit.add((c+a,d+b))
                            q.append((a+c, b+d))
  

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()