class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = set((0,0))
        heap = [[nums1[0] + nums2[0],(0,0)]]
        ans = []
        i,j = 0, 0
        while heap and len(ans) < k:
            su, (i,j) = heapq.heappop(heap)
            ans.append([nums1[i],nums2[j]])
            visited.add((i,j))
            if i+1 < len(nums1) and len(ans) < k and (i+1,j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j],(i+1, j)))
            if j+1 < len(nums2) and len(ans) < k and (i,j+1) not in visited: 
                heapq.heappush(heap, (nums1[i] + nums2[j+1],(i, j+1)))
        return ans