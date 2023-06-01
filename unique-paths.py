class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = defaultdict(int)
        def helper(row, col):
            if min(row, col) < 0 or row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if (row, col) not in d:  
                d[(row,col)] = helper(row+1, col) + helper(row, col+1)
            return d[(row,col)]
        return helper(0,0)