class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j] in grid[(i//3,j//3)]:
                    return False
                
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                grid[(i//3, j//3)].add(board[i][j])

        return True