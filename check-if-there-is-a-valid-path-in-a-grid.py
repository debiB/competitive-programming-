from typing import List
from collections import defaultdict

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        graph = unionFind(len(grid), len(grid[0]))
        directions = {(0, 1), (1, 0)}

        def inbound(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            return False

        right = {1: {1, 3, 5}, 2: {}, 3: {}, 4: {1, 3, 5}, 5: {}, 6: {1, 3, 5}}
        down = {1: {}, 2: {2, 5, 6}, 3: {2, 5, 6}, 4: {2, 5, 6}, 5: {}, 6: {}}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for inc_i, inc_j in directions:
                    if inbound(i + inc_i, j + inc_j) and grid[i + inc_i][j + inc_j] in right[grid[i][j]] and inc_j == 1:
                        graph.union((i, j), (i + inc_i, j + inc_j))
                    if inbound(i + inc_i, j + inc_j) and grid[i + inc_i][j + inc_j] in down[grid[i][j]] and inc_i == 1:
                        graph.union((i, j), (i + inc_i, j + inc_j))

        return graph.find((0, 0)) == graph.find((len(grid) - 1, len(grid[-1]) - 1))


class unionFind:
    def __init__(self, row, col):
        self.parent = defaultdict(int)
        for i in range(row):
            for j in range(col):
                self.parent[(i, j)] = (i, j)
        self.rank = [[0 for _ in range(col)] for _ in range(row)]

    def find(self, root):
        if root == self.parent[root]:
            return root
        self.parent[root] = self.find(self.parent[root])
        return self.parent[root]

    def union(self, root1, root2):
        r1X, r1Y = self.find(root1)
        r2X, r2Y = self.find(root2)
        if self.rank[r1X][r1Y] < self.rank[r2X][r2Y]:
            self.parent[(r1X, r1Y)] = (r2X, r2Y)
        elif self.rank[r1X][r1Y] > self.rank[r2X][r2Y]:
            self.parent[(r2X, r2Y)] = (r1X, r1Y)
        else:
            self.parent[(r2X, r2Y)] = (r1X, r1Y)
            self.rank[r1X][r1Y] += 1

    def is_connected(self, root1, root2):
        return self.find(root1) == self.find(root2)