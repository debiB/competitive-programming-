class Trie:
    def __init__(self):
        self.root = {}
        self.maxi = 0
    
    def insert(self, nums):
        num = bin(nums) 
        num = num[2:]

        while len(num) < 32:
            num = '0' + num
        
        curr =  self.root
        maxi = self.maxi
        for char in num:
            if int(char) in curr:
                curr = curr[int(char)]
            else:
                
                curr[int(char)] = {}
                curr = curr[int(char)]
                
        curr =  self.root
        store = ""
        for char in num:
            if curr:
                if (1 - int(char)) in curr:
                    store += str(1 - int(char))
                    curr =  curr[1 - int(char)]
                else:
                    store += char
                    curr =  curr[int(char)]
        compared = int(store, 2)
        self.maxi = max(self.maxi, nums ^ compared)
                

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        return trie.maxi