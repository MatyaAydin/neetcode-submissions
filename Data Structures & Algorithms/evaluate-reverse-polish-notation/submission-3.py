class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            print(st)
            if t  == "+":
                res1 = st.pop()
                res2 = st.pop()
                st.append(int(res1 + res2))
            elif t == "-":
                res1 = st.pop()
                res2 = st.pop()
                st.append(int(res2 - res1))
            elif t == "*":
                res1 = st.pop()
                res2 = st.pop()
                st.append(int(res1*res2))
            elif t == "/":
                res1 = st.pop()
                res2 = st.pop()
                st.append(int(res2 / res1))
            else:
                st.append(int(t))
        
        return st.pop()

        