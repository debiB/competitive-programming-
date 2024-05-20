class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        row = len(heights)
        col = len(heights[0])
        pacific = set()
        atlantic = set()
        ans = []
        def inbound(i,j):
            return 0 <= i < row and 0 <= j < col
        def dfs(r,c,prev,visited):  
            if (r,c) in visited or not inbound(r,c) or heights[r][c] < prev:
                return 
            visited.add((r,c))
            for dx,dy in directions:
                 dfs(r+dx,c+dy,heights[r][c], visited)
          
        for c in range(col):
            dfs(0,c,heights[0][c],pacific)
            dfs(row -1,c,heights[row-1][c],atlantic)
        for r in range(row):
            dfs(r,0,heights[r][0], pacific)
            dfs(r,col-1,heights[r][col-1], atlantic)
        for i in range(row):
            for j in range(col):
                if (i,j) in pacific and (i,j) in atlantic:
                    ans.append([i,j])
        
        return ans