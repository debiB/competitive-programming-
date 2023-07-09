class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = unionFind(len(source))
        h = 0
        for i,j in allowedSwaps:
            graph.union(i,j)
        d = defaultdict(list)
        for i in range(len(graph.parent)):
            d[graph.find(i)].append(i)
        for k in d.keys():
            idx = d[k]
            src = []
            des = []
            for j in idx:
                src.append(source[j])
                des.append(target[j])
            if not src == des:

                counter1 = Counter(src)
                counter2 = Counter(des)
                common_count = sum((counter1 & counter2).values())
                h += (len(src)-common_count)

        return h
class unionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*size
    def find(self, root):
        if root == self.parent[root]:
            return root
        self.parent[root] = self.find(self.parent[root])
        return self.parent[root]
    def union(self, root1,root2):
        px = self.find(root1)
        py = self.find(root2)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else: 
               self.parent[py] = px
               self.rank[px]+=1