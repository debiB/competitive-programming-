class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.count = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.d = defaultdict(int)
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        
        value = self.d[key] 

        for i in range(len(key)):
            idx = ord(key[i]) - ord("a")
            if not curr.children[idx]:
                curr.children[idx]  = TrieNode()
            curr = curr.children[idx]
            curr.count+=(val-value)
        self.d[key] = val 
    def sum(self, prefix: str) -> int:
        curr = self.root
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - ord("a")
            if  not  curr.children[idx]:
                return 0 
            else:
               curr = curr.children[idx]
        return curr.count  


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)