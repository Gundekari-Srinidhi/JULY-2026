class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        min1 = float("inf")
        sum1 = 0
        while r < n:
            sum1 += nums[r]
            while sum1 >= target and l < n:
                sum1 -= nums[l]
                min1 = min(min1,r - l + 1)
                l += 1   
            r += 1
        if min1 == float("inf"):
            return 0
        else:
            return min1
            

        