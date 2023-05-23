from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ans = ''
        graph = unionfind(s1, s2)
        for n in baseStr:
            if graph.find(n): 
                ans += graph.find(n)
        return ans

class unionfind:
    def __init__(self, size, size2):
        self.rep = {}
        for c1, c2 in zip(size, size2):
            self.union(c1, c2)
    def find(self, x):
        if x not in self.rep:
            return x
        if x != self.rep[x]:
            x = self.find(self.rep[x])
        return x
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            if parentX < parentY:
                self.rep[parentY] = parentX
            else:
                self.rep[parentX] = parentY