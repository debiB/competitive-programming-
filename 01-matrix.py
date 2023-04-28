class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = {(0,1), (1,0), (0,-1),(-1,0)}
        def inbound(i,j):
            if i >= 0 and i < len(mat) and j >= 0 and j < len(mat[0]):
                return True
            return False


        visited = set()
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]  == 0:
                    visited.add((i,j))
                    q.append((0,i,j))

        while q:
            dis, num1,num2 = q.popleft()
            mat[num1][num2] = dis
            for r,c in directions:
                if inbound(num1+r, num2+c) and (num1+r,num2+c) not in visited:
                    visited.add((num1+r,num2+c))
                    q.append((dis+1, num1+r,num2+c))

        return mat