class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        d = [poured]
        for _ in range(query_row):
            temp = [0]*(len(d)+1)
            for i in range(len(d)):
              if d[i] >=1:
                temp[i] += (d[i] - 1)/2
                temp[i+1] += (d[i] - 1)/2
            d = temp
        return min(1, d[query_glass])