class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = {(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)}
        i,j = click
        def inbound(x,y):
            if x>=0 and x < len(board) and y >= 0 and y< len(board[0]):
                return True
            return False
        count = 0
        def get(i,j):
            nonlocal count
            for a,b in directions:
                if inbound(i+a,j+b) and board[i+a][j+b] == 'M':
                    count+=1
            return count

        if not inbound(i,j) or not board:
            return board

        if board[i][j] == 'M':
            board[i][j] = 'X'

        else:
            n = get(i,j)
            if n:
                board[i][j] = str(n)
            else:
                board[i][j] = 'B'
                for a,b in directions:
                    if inbound(i+a,j+b) and board[i+a][j+b] != 'M' and board[i+a][j+b] != 'B':
                        self.updateBoard(board,[i+a,j+b])



        return board