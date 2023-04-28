class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = 0 
        n = len(matrix)-1
        while m < n:
             matrix[m], matrix[n] = matrix[n], matrix[m] 
             m+=1
             n-=1

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]