class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
          return -1
        diff = [g-c for g,c in zip(gas,cost)]
        total,start = 0,0
        for i in range(len(diff)):
            total+=diff[i]
            if total < 0:
                total= 0
                start = i+1
        return start