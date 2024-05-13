class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        in_idx = []
        ans = []
        for i,j in enumerate(intervals):
            in_idx.append([j,i])
        in_idx.sort()
       
        def search(num):
            start, end = 0, len(in_idx) -1
            ans = -1   
            while end >= start:
                mid = (start + end)//2
                if in_idx[mid][0][0] >= num:
                    if ans == -1 or (ans != -1 and in_idx[mid][0][0] < in_idx[ans][0][0]):
                        ans = in_idx[mid][1]
                    end = mid - 1
                else:
                    start = mid + 1
            return ans
        for i,j in intervals:
            ans.append(search(j))
        return ans
        