from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        d = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                d[i].append(graph[i][j])
       # print(d)
        def helper(idx,li):
            nonlocal ans
            if idx == len(graph) - 1:
                li.append(idx)
                ans.append(li.copy())
                return
            li.append(idx)
            for i in d[idx]:
                helper(i, li)
                li.pop()
        helper(0,[])
        return ans