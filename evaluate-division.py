class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        #ans = []
        
        for i,j  in enumerate(equations):
            a,b = j
            d[a].append((b,values[i])) 
            d[b].append((a,1/values[i]))
        print(d)
        def dfs(num, denum):
            if num not in d or denum not in d:
                return -1
            q, visit = deque(), set({num})
            q.append((num,1))
            #visit.add(num)
            while q:
                node, w = q.popleft()
                if node == denum:
                    return w
                for children, wei in d[node]:
                    if children not in visit:
                        q.append((children, wei*w))
                        visit.add(children)
            return -1
        return [dfs(i,j) for i,j in queries]