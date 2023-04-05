class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans= 0
        players.sort()
        trainers.sort()
        i,j = 0, 0
    #$l = min(len(players), len(trainers))
        while i < len(players) and j < len(trainers):
            if players[i] > trainers[j] and j < len(trainers):
                j+=1
            else:
                ans+=1
                i+=1
                j+=1
        return ans
