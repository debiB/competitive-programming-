class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        indeg =[0]*len(quiet)
        ans = [i for i in range(len(quiet))]
        d = defaultdict(list)
        for r,p in richer:
            d[r].append(p)
            indeg[p]+=1
        q = deque()
        for k in range(len(quiet)):
            if indeg[k] == 0:
                q.append(k)
        while q:
            r = q.popleft()
            qui = ans[r]
            for children in d[r]:
                qui_p = ans[children]
                ans[children] = min(qui_p, qui, key = lambda per: quiet[per])
                indeg[children]-=1
                if indeg[children] == 0:
                    q.append(children)

        return ans