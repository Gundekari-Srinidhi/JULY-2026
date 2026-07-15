class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a=0
        b=0
        for i in range(1,(n*2)+1):
            if i%2==0:
                b+=i
            else:
                a+=i
        while b!=0:
            a,b=b,a%b
        return a

        