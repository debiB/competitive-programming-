class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        li = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            li[len(matrix)-1][i] = matrix[len(matrix)-1][i]
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix[0])):
                
                if j >= 1 and j < len(matrix[0]) - 1:
                    li[i][j] = matrix[i][j]+min(li[i+1][j-1], li[i+1][j+1],li[i+1][j])
                elif j == 0:
                    li[i][j] = matrix[i][j]+min(li[i+1][j+1],li[i+1][j])
                else:
                   li[i][j] = matrix[i][j]+min(li[i+1][j-1],li[i+1][j]) 
        
        return min(li[0])