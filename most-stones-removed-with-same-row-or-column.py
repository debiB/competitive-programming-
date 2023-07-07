class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rowL = -1
        colL = -1
        for i in stones:
            rowL = max(rowL,i[0])
            colL = max(colL,i[1])
        print(rowL+colL+2)
        graph = unionFind(rowL+colL+2)
        for i in stones:
            print(i[0],i[1]+rowL+1)
            graph.union(i[0],i[1]+rowL+1)
        return len(stones) - graph.components()


class unionFind:
    def __init__(self, length):
        self.parent = {}
        self.rank = [0]*(length)
    def find(self, root):
        if root not in self.parent:
            self.parent[root] = root
            return root
        elif root != self.parent[root]:
            self.parent[root] = self.find(self.parent[root])
        return self.parent[root]
    def union(self, root1, root2):
        parX = self.find(root1)
        parY = self.find(root2)
        if self.rank[parX] > self.rank[parY]:
            self.parent[parY] = parX
        elif self.rank[parX] < self.rank[parY]:
            self.parent[parX] = parY
        else:
            self.parent[parY] = parX
            self.rank[parX]+=1
    def components(self):
        num = set()
        for i in self.parent:
           num.add(self.find(i))
        print(num)
        return len(num)