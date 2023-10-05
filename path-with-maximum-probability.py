class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        prob = [0]*n
        # for i in range(len(succProb)):
        #     prob[edges[i][0]] = succProb[i]
        #     prob[edges[i][1]] = succProb[i]
        prob[start_node] = 1
        
        for j in range(n-1):
            has_update = 0
            for i in range(len(edges)):
                u,v = edges[i]
                w = succProb[i]
                if prob[u]*w > prob[v]:
                    prob[v] = prob[u]*w 
                    has_update = 1
                if prob[v]*w > prob[u]:
                    prob[u] = prob[v]*w
                    has_update = 1
            if not has_update:
                break
        return prob[end_node]