class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.num = nums 
        heapq.heapify(self.num)
        while len(self.num) > k:
            heapq.heappop(self.num)

    def add(self, val: int) -> int:
        heapq.heappush(self.num, val)
        if len(self.num) > self.kth:
            heapq.heappop(self.num)
        return self.num[0]


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)