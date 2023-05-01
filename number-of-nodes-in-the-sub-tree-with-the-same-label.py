class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0]*n
        d = defaultdict(list)
        for e1, e2 in edges:
            d[e1].append(e2)
            d[e2].append(e1)
        visited = set()
        def dfs(node):
            nonlocal ans
            visited.add(node)
            cnt = collections.Counter()
            for n in d[node]:
                if n not in visited:
                    cnt+=dfs(n)
            cnt[labels[node]]+=1
            ans[node] = cnt[labels[node]]
            return cnt
        dfs(0)
        return ans