class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)
        arr = [(-count, w) for w, count in d.items()]
        heapq.heapify(arr)
        return [heapq.heappop(arr)[1] for _ in range(k)]