class Solution(object):
    def climbStairs(self, n, costs):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in xrange(1, n + 1):
            for j in xrange(max(0, i - 3), i):
                dp[i] = min(dp[i], dp[j] + costs[i - 1] + (i - j) ** 2)

        return dp[n]