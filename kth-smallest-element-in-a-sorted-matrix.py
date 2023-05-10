class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flattend = [ele for row in matrix for ele in row]
        heapq.heapify(flattend)
        for _ in range(k-1):
                heapq.heappop(flattend)
        return flattend[0]