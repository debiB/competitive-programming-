class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = {}
        ans = []
        _len = n*2
        possible_strings = ["(", ")"]
        def backtrack(string, l_count, r_count):
            nonlocal ans
            if len(string) ==  _len:
                if l_count == r_count:
                    ans.append(string[::])
                return 
            for i in possible_strings:
                if i == ")" and l_count > r_count:
                    backtrack(string + ")", l_count, r_count + 1)
                if i == "(":
                    backtrack(string + "(", l_count + 1, r_count)
        backtrack("",0, 0)
        return ans
            
                


        