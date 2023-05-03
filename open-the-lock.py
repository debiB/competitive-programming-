class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in deadends:
            return -1
        def getch(a):
            res = []
            for i in range(4):
                n = int(a[i])
                digit = str((n+1)%10)
                res.append(dig[:i]+digit+dig[i+1:])
                digit = str((n-1+10)%10)
                res.append(dig[:i]+digit+dig[i+1:])
            return res

        q = deque([("0000", 0)])
        while q:
            dig, path = q.popleft()
            if dig == target:
                return path
            for ch in getch(dig):
                if ch not in visited:
                    q.append((ch, path+1))
                    visited.add(ch)

        return -1