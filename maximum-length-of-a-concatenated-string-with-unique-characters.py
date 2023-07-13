class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char = set()
        def has_common(char,s):
            c = Counter(char) + Counter(s)
            return max(c.values()) > 1
        def backtrack(idx):
            if idx >= len(arr):
                return len(char)
            res = 0
            if not has_common(char, arr[idx]):
                for a in arr[idx]:
                    char.add(a)
                res = backtrack(idx+1)
                for a in arr[idx]:
                    char.remove(a)
            return max(res, backtrack(idx+1))
        return backtrack(0)