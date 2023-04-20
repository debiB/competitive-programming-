class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        mat = [[] for _ in range(n)]

        for u,v in roads:
            mat[u].append(v)
            mat[v].append(u)
        deg = [len(mat[i]) for i in range(n)]
        m=0
        for i in range(n):
            for j in range(i+1,n):
                cnt = deg[i] + deg[j] - (1 if j in mat[i] else 0)
                m= max(m, cnt)
        return m