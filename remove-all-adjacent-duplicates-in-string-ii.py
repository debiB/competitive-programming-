class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        idx = 0
        while idx < len(s):
            if st and st[-1][0] == s[idx]:
                st[-1][1]+=1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([s[idx],1])
            idx+=1
        return "".join(char*count for char,count in st)