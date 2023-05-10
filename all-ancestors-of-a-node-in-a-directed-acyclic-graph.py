class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        indeg = [0]*n
        q = deque()
        ans = [set() for _ in range(n)]
        for i,j in edges:
            d[i].append(j)
            indeg[j]+=1
        for k in range(n):
            if indeg[k] == 0:
                q.append(k)
        while q:
            res = q.popleft()
            for child in d[res]:
                
                ans[child].add(res)
                if len(ans[res]) > 0:
                    ans[child].update(ans[res])

                indeg[child]-= 1

                if indeg[child] == 0:
                    q.append(child)
        for lst in range(len(ans)):
            ans[lst] = list(ans[lst])
        for lst in ans:
            lst.sort()
        return ans