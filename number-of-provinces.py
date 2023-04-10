from collections import defaultdict
class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        visited = set()
        count = 0
        d = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    d[i+1].append(j+1)
        print(d)
        def helper(num):
            nonlocal count
            if num in visited:
                return
            visited.add(num)
            for key in d[num]:
                if key not in visited:
                    helper(key)
        for i in range(1,len(matrix)+1):
            if i not in visited:
                helper(i)
                count+=1
      
        return count