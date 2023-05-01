class Solution:
    def solve(self, boards: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = {(1,0),(0,1),(-1,0),(0,-1)}
        def dfs(i,j):
            if i < 0 or i >= len(boards) or j < 0 or j >= len(boards[0]) or boards[i][j] == 'X':
                return
            boards[i][j] = 'T'
            for a,b in directions:
                if i+a >= 0 and i+a < len(boards) and j+b >= 0 and j+b < len(boards[0]) and boards[i+a][j+b] == 'O':
                    boards[i+a][j+b] = 'T'
                    dfs(i+a, j+b)
                
        for r in range(len(boards)):
           for c in range(len(boards[0])):
               if boards[r][c] == 'O' and r in [0, len(boards)-1] or c in [0,len(boards[0]) - 1]:
                   dfs(r,c)
        
        for r in range(len(boards)):
            for c in range(len(boards[0])):
                if boards[r][c] == 'O':
                   boards[r][c] = 'X'

        for r in range(len(boards)):
            for c in range(len(boards[0])):
               if boards[r][c] == 'T':
                   boards[r][c] = 'O'