class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def valid_4(s):
            nums = s.split(".")
            for x in nums:
                if len(x) == 0 or len(x) > 3:
                    return "Neither"
                if x[0] == "0" and len(x) > 1 or not x.isdigit() or int(x) > 255:
                    return "Neither"
            return "IPv4"
        def valid_6(s):
            nums = s.split(":")
            hexdigits = '0123456789abcdefABCDEF'
            for x in nums:
                if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                    return "Neither"
            return "IPv6"

        if queryIP.count(".") == 3:
            return valid_4(queryIP)
        elif queryIP.count(":") == 7:
            return valid_6(queryIP)
        else:
            return "Neither"