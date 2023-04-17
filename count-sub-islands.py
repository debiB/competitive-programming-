class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count= 0 
        visited = set()
        directions = {(1,0), (-1,0), (0,1), (0,-1)}
        
        def dfs(i,j):
            if i < 0 or i>= len(grid2) or j < 0 or j>= len(grid2[0]) or grid2[i][j] == 0 or (i,j) in visited:
                return True
            visited.add((i,j))
            res = True
            if grid1[i][j] == 0:
                res = False
            for dir1, dir2 in directions:
                res = dfs(i+dir1,j+dir2) and res
            return res
        for a in range(len(grid2)):
            for b in range(len(grid2[0])):
                if grid2[a][b] == 1 and (a,b) not in visited and dfs(a,b):
                    count+=1
        return count