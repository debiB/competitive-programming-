class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        l = len(board)
        board.reverse()
        print(board)
        def inbound(i,j):
            if 0<=i<l and 0<=j<l:
                return True
            return False
        def pair(num):
            r = (num-1)//l
            c = (num-1)%l
            if r%2:
                c = l-c-1
            return [r,c]

        q = deque([(1, 0)])
        visited = set()
        while q:
            a, path = q.popleft()
            for i in range(1,7):
                di = a+i
                r,c = pair(di)
                if inbound(r,c) and board[r][c] != -1:
                    di = board[r][c]
                if di  == l*l:
                    return path+1
                if di not in visited:
                    q.append((di,path+1))
                    visited.add(di)
        return -1