class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = defaultdict(int)
        rank = defaultdict(int)
        def find(x):
            root = x
            while root != rep[root]:
                root = rep[root]
            while x != root:
                parent = rep[x]
                rep[x] = root
                x = parent
            return root
        for i,j in edges:
            rep[i] = i
            rep[j] = j
        for x,y in edges:
            parX = find(x)
            parY = find(y)
            if parX == parY:
                return [x,y]
            elif parX != parY:
                if rank[x] < rank[y]:
                    rep[parX] = parY
                elif rank[x] > rank[y]:
                    rep[parY] = parX
                else:
                    rep[parX] = parY
                    rank[parY] +=1