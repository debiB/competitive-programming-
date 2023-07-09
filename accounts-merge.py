from collections import defaultdict, Counter
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ans = []
        graph = UnionFind(len(accounts))
        
        for i in range(len(accounts)):
            for j in range(i+1, len(accounts)):
                if accounts[i][0] == accounts[j][0]: 
                    sub1 = accounts[i][1:]
                    sub2 = accounts[j][1:]
                    count1 = Counter(sub1)
                    count2 = Counter(sub2)
                    common = sum((count1 & count2).values())
                    if common:
                        graph.union(i, j)
        
        d = defaultdict(list)
        
        for i in range(len(accounts)):
            d[graph.find(i)].append(i)
        
        for k in d.keys():
            idx = d[k][0]
            li = set()
            
            for i in d[k]:
                li.update(accounts[i][1:])
            
            li = list(li)
            #print(li)
            li.sort()
            li.insert(0, accounts[idx][0])
            ans.append(li)
        ans.sort(key=lambda x: x[0])
        return ans



class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*size
    
    def find(self, root):
        if root == self.parent[root]:
            return root
        self.parent[root] = self.find(self.parent[root])
        return self.parent[root]
    
    def union(self, root1, root2):
        px = self.find(root1)
        py = self.find(root2)
        
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1