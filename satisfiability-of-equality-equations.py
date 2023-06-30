class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = unionFind(26)
        n_equal = []
        for i in equations:
            if i[1] == "!":
                if graph.find(ord(i[0]) - 97) == graph.find(ord(i[-1]) - 97):
                    return False
                else:
                    n_equal.append(i)
            else:
                graph.union(ord(i[0]) - 97,ord(i[-1]) - 97)
        for j in n_equal:
            if graph.find(ord(j[0]) - 97) == graph.find(ord(j[-1]) - 97):

                return False
        return True

class unionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*26
    def find(self, root):
        if root == self.parent[root]:
            return root
        self.parent[root] = self.find(self.parent[root]) 
        return self.parent[root]
    def union(self, root1,root2):
        parX = self.find(root1)
        parY = self.find(root2)
        if self.rank[parX] > self.rank[parY]:
            self.parent[parY] = parX
        elif self.rank[parX] < self.rank[parY]:
            self.parent[parX] = parY
        else:
            self.parent[parX] = parY
            self.rank[parY]+=1