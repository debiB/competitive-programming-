class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        max_score = defaultdict(int)
        for i in range(len(questions)-1, -1,-1):
            max_score[i] = max(questions[i][0] + max_score[i+1+ questions[i][1]] , max_score[i+1])
        return max_score[0]