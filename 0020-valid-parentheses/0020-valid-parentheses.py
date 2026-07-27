class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if st and ((i == ")" and st[-1] == "(") or (i == "}" and st[-1] == "{") or (i == "]" and st[-1] == "[")):
                st.pop()
            else:
                st.append(i)
        return len(st) == 0
        