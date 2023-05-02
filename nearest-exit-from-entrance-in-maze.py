class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isValid(i,j):
            if i >= 0 and i < len(maze) and j >= 0 and j < len(maze[0]) and maze[i][j] == ".":
                return True
            return False 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        while q:
            a,b,path = q.popleft()
            if (a == 0 or a == len(maze)-1 or b == 0 or b == len(maze[0])-1) and (a,b) != (entrance[0], entrance[1]):
                        return path
            for i,j in directions:
                if isValid(a+i,b+j):
                    q.append((a+i,b+j,path+1))
                    maze[a+i][b+j] = "+"
        return -1