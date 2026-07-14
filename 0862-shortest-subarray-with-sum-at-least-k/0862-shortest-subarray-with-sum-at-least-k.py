class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        dq = []
        ans = float("inf")
        for i in range(n+1):
            while dq and (prefix[i] - prefix[dq[0]]) >= k:
                ans = min(ans,i - dq.pop(0))
            
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)

        if ans == float("inf"):
            return -1
        else:
            return ans

        