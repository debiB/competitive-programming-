class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        prev = [[0 for _ in range(len(nums2) + 2)]  for _ in range(len(nums1) + 2)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    prev[i+1][j+1] = 1 + prev[i][j]
                else:
                    prev[i+1][j+1] = max(prev[i+1][j], prev[i][j+1]) 
        return prev[len(nums1)][len(nums2)]