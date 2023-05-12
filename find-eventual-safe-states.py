class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        d = {}
        ans = []
        def dfs(i):
            if i in d:
                return d[i]
            d[i] = False
            for child in graph[i]:
                if not dfs(child):
                    return False
            d[i] = True
            return True
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans