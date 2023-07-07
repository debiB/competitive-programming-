class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calc(i,j):
            return abs(i[0] - j[0]) + abs(i[1] - j[1])
        graph = unionFind(len(points))
        path = []
        ans = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = calc(points[i],points[j])
                path.append([d,i,j])
        path.sort()
        for dis,i,j in path:
            if graph.union(i,j):
                ans+=dis
        return ans

class unionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*size
    def find(self, root):
        if root != self.parent[root]:
            self.parent[root] = self.find(self.parent[root])
        return self.parent[root]
    def union(self,root1, root2):
        px = self.find(root1)
        py = self.find(root2)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px]+=1
            return True
        else:
            return False