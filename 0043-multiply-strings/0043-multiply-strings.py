class Solution:
    def fun(self,num):
        ans = 0
        for i in num:
            ans = ans * 10 + (ord(i) - ord('0'))
        return ans
    def fun1(self,val):
        res = ""
        while val > 0:
            rem = val % 10
            res = chr(rem + ord('0')) + res
            val //= 10
        return res

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        ans1=self.fun(num1)
        ans2=self.fun(num2)
        val = ans1*ans2
        return self.fun1(val)