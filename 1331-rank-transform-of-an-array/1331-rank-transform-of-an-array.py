class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return arr
        val = sorted(arr)
        d= {val[0] : 1}
        for i in range(1,len(val)):
            if val[i] not in d:
                d[val[i]] = d[val[i-1]]+1
        l = []
        for i in arr:
            l.append(d[i])
        return l


        