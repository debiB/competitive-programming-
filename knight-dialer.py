class Solution:
    def knightDialer(self, n: int) -> int:
        matrix = [[4,6], [6,8], [7,9], [4,8], [0,3,9],[],[0,1,7],[2,6],[1,3], [2,4]]
        ans = 0
        dp = defaultdict(int)
        def enum(moves, num):
            if moves == 0:
                return 1
            if (moves,num) not in dp:
                for child in matrix[num]:
                    dp[(moves, num)]+= enum(moves-1, child)
            return dp[(moves,num)]
        for i in range(10):
            ans+=enum(n-1,i)
        #print(dp)
        return ans%(pow(10,9)+7)