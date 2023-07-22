class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word = 0
        arr = [0]*len(words)
        for i in range(len(words)):
            num = 0 
            for j in words[i]:
                num |= (1<<(ord(j) - 97))
            arr[i] = num
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]& arr[j] == 0:
                    length = len(words[i])*len(words[j])
                    word = max(word, length)
        return word