class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d = {"(":")"}
        st = [0]
        for i in s:
            if i == ")":
                if st[-1] == 0:
                    st.pop()
                    st[-1] += 1
                else:
                    val = st.pop()
                    st[-1] += val * 2
            else:
                st.append(0)    
        return st[-1]
        