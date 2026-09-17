class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1
        dp = [INF] * (n + 1)
        dp[0] = INF

        left = 0
        total = 0
        ans = INF

        for right in xrange(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if dp[left] < INF:
                    ans = min(ans, length + dp[left])

                dp[right + 1] = min(dp[right], length)
            else:
                dp[right + 1] = dp[right]

        return -1 if ans == INF else ans