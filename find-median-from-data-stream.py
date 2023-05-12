class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)


    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        num = heapq.heappop(self.minHeap)
        heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            num = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -num)
        

    def findMedian(self) -> float:
        n = -self.maxHeap[0]
        if len(self.maxHeap) == len(self.minHeap):
            med = (self.minHeap[0]+n)/2
        else:
            med = n
        return med
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()