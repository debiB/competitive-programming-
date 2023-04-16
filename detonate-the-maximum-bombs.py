from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res = 0
        #visited = set()
        d = defaultdict(list)
        for i in range (len(bombs)):
            for j in range(len(bombs)):
                if i!= j and bombs[i][2] >= math.sqrt((bombs[i][0]- bombs[j][0])**2 + (bombs[i][1]- bombs[j][1])**2):
                    d[i].append(j)

        def dfs(i, visited):
            for l in d[i]:
                if l not in visited:
                    visited.add(l)
                    dfs(l, visited)
        for k in range(len(bombs)):
            visited = set([k])
            dfs(k,visited)
            res= max(res, len(visited))
        return res