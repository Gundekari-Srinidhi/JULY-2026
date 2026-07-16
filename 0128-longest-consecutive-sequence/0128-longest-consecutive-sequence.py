class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 1
        count = 0
        max1 = 0
        arr = set(arr)
        for i in arr:
            if i-1 not in arr:
                val = i
                count = 1
                while val+1 in arr:
                    count += 1
                    val += 1
                max1 = max(count,max1)
                count = 1
        return max1
        