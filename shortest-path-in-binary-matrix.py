class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = {(0,1), (0,-1), (1,0), (-1, 0), (1,1), (-1, -1), (1,-1), (-1,1)}
        path = 1
        if len(grid) == 1 and grid[0][0] == 0:
            return 1
        if grid[0][0] == 1:
            return -1
        def inbound(i,j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                return True
            return False
        visited = set()
        q = deque([(0,0,1)])
        while q:
            c = len(q)
            path+=1
            for _ in range(c):
                num1, num2, currpath= q.popleft()
                for i,j in directions: 
                    if inbound(num1+ i,num2+ j) and (num1+i,num2+j) not in visited and grid[num1+i][num2+j] == 0:
                        if (num1+i,num2+j) == (len(grid)-1, len(grid[0]) -1):
                            return currpath +1
                        q.append((num1+i, num2+j,currpath + 1))
                        visited.add((num1+ i,num2+ j))
        return -1