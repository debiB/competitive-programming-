class Solution:
    def getOrder(self, task: List[List[int]]) -> List[int]:
        for i, t in enumerate(task):
           t.append(i)
        task.sort(key = lambda x:x[0])
        res, heap = [], []
        num, time = 0, task[0][0]
        while heap or num < len(task):
            while num < len(task) and time >= task[num][0]:
                heapq.heappush(heap, (task[num][1],task[num][2]))
                num+=1
            if not heap and  i< len(task):
                time = task[num][0]
            else:
                el_time, idx = heapq.heappop(heap)
                time+=el_time
                res.append(idx)
        return res