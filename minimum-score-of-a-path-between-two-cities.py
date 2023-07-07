class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = [i for i in range(n+1)]
        rank = [0]*(n+1)
        def find(num):
            root = num 
            while root != rep[root]:
                root = rep[root]
            while num != root:
                par = rep[num]
                rep[num] = root
                num = par
            return rep[root]   
        def union(num1, num2):
            parX = find(num1)
            parY = find(num2)
            if rank[parX] < rank[parY]:
                rep[parY] = parX
            else:
                rep[parY] = parX
                rank[parX]+=1
        def isconnected(root1, root2):
            return find(root1) == find(root2)

        _min = float("inf")
        for i,j,k in roads:
            union(i,j)
        for i,j,k in roads:
            if isconnected(1,i) or isconnected(1,j):
                _min = min(k,_min)
        return _min