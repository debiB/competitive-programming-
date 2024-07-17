
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_num(li, lj, hi, hj):
            if li > hi or lj > hj:
                return False

            mid_i = (li + hi) // 2
            mid_j = (lj + hj) // 2

            if matrix[mid_i][mid_j] == target:
                return True
            elif matrix[mid_i][mid_j] < target:
                return find_num(mid_i + 1, lj, hi, mid_j) or find_num(li, mid_j + 1, hi, hj)
            else:
                return find_num(li, lj, mid_i - 1, hj) or find_num(mid_i, lj, hi, mid_j - 1)
        
        if not matrix or not matrix[0]:
            return False
        
        return find_num(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
