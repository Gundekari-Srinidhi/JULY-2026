class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        def fun(n,res,ans):
            if n == 0:
                return res 
            res = ""
            count = 1
            for i in range(len(ans)-1):
                if ans[i] == ans[i+1]:
                    count += 1
                else:
                    res += str(count)
                    res += ans[i]
                    count = 1
            res += str(count)
            res += ans[-1]
            ans = res
            return fun(n-1,res,ans)
        return fun(n-1,"","1")