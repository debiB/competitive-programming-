class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        k = len(needle)
        target_window, window = 0, 0
        base = 27
        mod = 10**9 + 7

        
        for i in range(k):
            num = ord(needle[i]) - 96
            target_window = (target_window * base + num) % mod
            num = ord(haystack[i]) - 96
            window = (window * base + num) % mod

        if window == target_window:
            return 0

        base_k_minus_1 = pow(base, k - 1, mod)

        for i in range(k, len(haystack)):
           
            num = ord(haystack[i - k]) - 96
            window = (window - num * base_k_minus_1) % mod

          
            num = ord(haystack[i]) - 96
            window = (window * base + num) % mod

            if window == target_window:
                return i - k + 1

        return -1