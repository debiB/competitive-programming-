class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.count = 0
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.count+=1
        curr.isEnd = True
    def find(self, word):
        curr = self.root
        ans = 0
        for i in range(len(word)):
            idx = ord(word[i]) - ord("a")
            curr = curr.children[idx]
            ans += curr.count
        return ans



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        li = []
        for word in words:
            trie.insert(word)
        for word in words:
            li.append(trie.find(word))
        return li