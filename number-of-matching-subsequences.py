class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isEnd = True
        curr.freq+=1
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = 0
        
        def find(idx, ch):
            for i in range(idx, len(s)):
                if s[i] == ch:
                    return i
            return -1
        
        def dfs(i, node):
            nonlocal ans
            if node.isEnd:
                ans += node.freq
            
            for j in range(26):
                if node.children[j]:
                    idx = find(i, chr(97 + j))
                    if idx != -1:
                        dfs(idx+1, node.children[j])
        
        dfs(0, trie.root)
        
        return ans