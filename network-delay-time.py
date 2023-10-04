class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        d_ans = [float("inf") for _ in range(n+1)]

        d_ans[k], d_ans[0] = 0, 0
        for ed1, ed2, w in times:
            d[ed1].append((ed2,w))
        print(d)
        heap = []
        heapq.heappush(heap, (0,k))
        visited = set()
        while heap:
            distance, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for i,j in d[node]:
                k = distance + j
                if k < d_ans[i]:
                    d_ans[i] = k
                    heapq.heappush(heap, (k,i))
        return max(d_ans) if max(d_ans) != float("inf") else -1