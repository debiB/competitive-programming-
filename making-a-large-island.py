class Solution:
    def largestIsland(self, matrix: List[List[int]]) -> int:
        id = 2
        d = defaultdict(int)
        def inbound(i,j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])
        direction = {(0,1),(0,-1),(1,0),(-1,0)}
        def bfs(i,j):
        
            ans = 1
            q = deque()
            q.append((i,j))
            visited = set()
            visited.add((i,j))
            matrix[i][j] = id
            while q:
                i,j = q.popleft()
                for dx, dy in direction:
                    if inbound(i+dx, j + dy) and (i+dx, j + dy) not in visited and matrix[i+dx][j + dy] == 1:
                        matrix[i+dx][j+dy] = id
                        visited.add((i+dx, j + dy))
                        q.append((i+dx, j + dy))
                        ans+=1
            
            return ans
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    area = bfs(i,j)
                    d[id] = area
                    id+=1
        _max = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                surr = set()
                ans = 0
                if matrix[i][j] == 0:
                    
                    for dx,dy in direction:
                        if inbound(i+dx,j+dy):

                            surr.add(matrix[i+dx][j+dy])
    
                    for k in surr:
                        ans+=d[k]
                    _max = max(_max, ans+1)
                else:
                    _max = max(_max, d[matrix[i][j]])
        return _max