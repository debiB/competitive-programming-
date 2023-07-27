class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            d = heights[i+1] - heights[i]
            if d > 0:
                if d <= bricks:
                    heapq.heappush(heap,-d)
                    bricks-= d
                elif ladders > 0:
                    if heap and -heap[0] > d:
                        bricks += -heapq.heappop(heap)
                        heapq.heappush(heap, -d)
                        bricks -= d
                    ladders-=1
                else:
                    return i
        return len(heights) - 1