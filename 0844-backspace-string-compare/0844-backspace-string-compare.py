class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def fun(s):
            st = []
            for i in s:
                if i == "#" and st:
                    st.pop()
                elif i != "#":
                    st.append(i)
            return st
        return fun(s) == fun(t)


        