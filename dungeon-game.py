class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon[0]), len(dungeon)
        li = [[0 for _ in range(n)] for _ in range(m)]
        li[m-1][n-1] = max(1,1-dungeon[m-1][n-1])
        for r in range(m-2,-1,-1):
            li[r][n-1] = max(1, li[r+1][n-1] - dungeon[r][n-1])
        for c in range(n-2,-1,-1):
            li[m-1][c] = max(1, li[m-1][c+1] -dungeon[m-1][c]  )
        for i in range(m-2, -1,-1):
            for j in range(n-2,-1,-1):
                li[i][j] = min(li[i+1][j], li[i][j+1]) -  dungeon[i][j]
                if li[i][j] <= 0:
                    li[i][j] = 1
        return li[0][0]