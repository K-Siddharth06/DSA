class Solution(object):
    def numDistinct(self, s, t):
        m = len(t)
        dp = [0] * (m + 1)
        dp[0] = 1

        for c in s:
            for j in xrange(m - 1, -1, -1):
                if c == t[j]:
                    dp[j + 1] += dp[j]

        return dp[m]