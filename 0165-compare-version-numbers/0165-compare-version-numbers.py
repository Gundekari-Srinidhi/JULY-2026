class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        val1 = version1.split(".")
        val2 = version2.split(".")
        n = len(val1)
        m = len(val2)
        min1 = min(len(val1),len(val2))
        for i in range(min1):
            if int(val1[i]) < int(val2[i]):
                return -1
            elif int(val1[i]) > int(val2[i]):
                return 1
        while n > m:
            if int(val1[m]) > 0:
                return 1
            m += 1
        while n < m:
            if int(val2[n]) > 0:
                return -1
            n += 1
        return 0
            