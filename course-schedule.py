class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans = 0
        d = defaultdict(list)
        q = deque()
        indeg = [0]*numCourses
        for i,j in prerequisites:
            d[j]. append(i)
            indeg[i]+=1
        for i  in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while q:
            res = q.popleft()
            ans += 1
            for n in d[res]:
                indeg[n] -=1
                if indeg[n] == 0:
                    q.append(n)
        if ans == numCourses:
            return True
        else:
            return False