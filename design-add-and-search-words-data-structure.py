class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            idx = ord(i) - ord("a")
            if not curr.children[idx]:
                    curr.children[idx]= TrieNode()
            curr = curr.children[idx]
        curr.isEnd = True

    def search(self, words: str) -> bool:
        def dfs(i,curr):
            if i  == len(words):
                return curr.isEnd
            if words[i] == ".":
                for idx in range(26):
                    if curr.children[idx] and dfs(i+1,curr.children[idx]):
                            return True
                return False        
            else:
                index = ord(words[i]) - ord("a")
                if not curr.children[index]:
                    return False
                
                return  dfs(i+1, curr.children[index])
    
        return dfs(0, self.root)
            




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)