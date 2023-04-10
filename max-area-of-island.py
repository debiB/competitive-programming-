class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        _maxarea = 0
        def helper(row,col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0 or visited[row][col] == True:
                return 0
            visited[row][col] = True
            area = helper(row+1, col)
            area+= helper(row, col+1)
            area+= helper(row-1, col)
            area+= helper(row, col-1) 
            return area+1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    a = helper(i,j)
                    _maxarea = max(a, _maxarea)
        return _maxarea