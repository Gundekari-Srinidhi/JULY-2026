class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        ans = 0
        dp = [0] * n

        for i in range(m-1,n):
            if sequence[i-m+1:i+1] == word:
                if i >= m:
                    dp[i] = dp[i-m] + 1
                else:
                    dp[i] = 1
                ans = max(ans,dp[i])

        return ans