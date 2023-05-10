class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for _ in range(k):
            n = heapq.heappop(piles)
            x = -n -((-n)//2)
            heapq.heappush(piles,-x)
        return -1*sum(piles)