class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]):

        ls = sorted(intervals, key=lambda x: (x[0], -x[1]))

        val = [ls[0]]

        for i in range(1, len(ls)):
            v1 = ls[i]
            v2 = val[-1]          

            if v2[0] <= v1[0] and v2[1] >= v1[1]:
                continue          
            else:
                val.append(v1)

        return len(val)