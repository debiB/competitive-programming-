class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        #self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord("a")
            if not curr.children[idx] and i == len(word)-1:
                curr.children[idx] = TrieNode()
                return True
            elif not curr.children[idx] and i < len(word)-1:
                return False
            curr = curr.children[idx] 

class Solution: 
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        ans = ""
        words.sort()
        for word in words:
            c = trie.insert(word)
            if c  and len(word) > len(ans):
                    ans = word
        return ans