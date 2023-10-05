class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word,idx):
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
            curr.idx = idx
            
    def startsWith(self,prefix, suffix):
        curr = self.root
        word = suffix + "#" + prefix
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return -1
        return curr.idx
            

class WordFilter:

    def __init__(self, words: List[str]):
        self.suffix = Trie()
        self.rem = defaultdict(list)
        for i, w in enumerate(words):
            tmp = w + "#" + w
            for j in range(len(w)):
                self.suffix.insert(tmp[j:],i)
        

    def f(self, pref: str, suff: str) -> int:
        if (pref, suff) not in self.rem:
            self.rem[(pref,suff)] = self.suffix.startsWith(pref, suff)
        return self.rem[(pref,suff)]  


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)