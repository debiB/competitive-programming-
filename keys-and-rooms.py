class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque()
        for a in rooms[0]:
            q.append(a)
        while q:
            n = len(q)
            for _ in range(n):
                num = q.popleft()
                if num not in visited and num != 0:
                    visited.add(num)
                    for b in rooms[num]:
                       # b = 0 
                        q.append(b)
        return len(visited) == len(rooms) - 1