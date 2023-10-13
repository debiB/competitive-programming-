class Solution:
    def numTeams(self, rating: List[int]) -> int:
        less = [0] * len(rating)
        greater = [0] * len(rating)
        ans = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)): 
                if rating[i] > rating[j]:
                    less[i] += 1
                elif rating[i] < rating[j]:
                    greater[i] += 1
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):  
                if rating[i] > rating[j]:
                    ans += less[j]
                elif rating[i] < rating[j]:
                    ans += greater[j]
        return ans