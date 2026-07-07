class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        sum1 = 0
        s = ""
        while n != 0:
            rem = n%10
            if rem != 0:
                sum1 += rem
                s += str(rem)
            n = n // 10
        s = s[::-1]
        return sum1*int(s)
        