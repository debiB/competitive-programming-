class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        d = defaultdict(int)
        def helper(i,j):
            if i >= len(triangle):
                return 0
            if i == len(triangle) - 1:
                return triangle[i][j]

            if (i,j) not in d:
                d[(i,j)] = triangle[i][j]+ min(helper(i+1,j),helper(i+1,j+1))
            return d[(i,j)]
        return helper(0,0)