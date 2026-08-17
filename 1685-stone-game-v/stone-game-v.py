class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[-1] * n for _ in range(n)]

        def solve(left, right):
            if left >= right:
                return 0

            if dp[left][right] != -1:
                return dp[left][right]

            ans = 0
            left_sum = 0
            right_sum = prefix[right + 1] - prefix[left]

            for mid in range(left, right):
                left_sum += stoneValue[mid]
                right_sum -= stoneValue[mid]

                if left_sum < right_sum:
                    if ans >= left_sum * 2:
                        continue

                    ans = max(ans, left_sum + solve(left, mid))

                elif left_sum > right_sum:
                    if ans >= right_sum * 2:
                        break

                    ans = max(ans, right_sum + solve(mid + 1, right))

                else:
                    ans = max(
                        ans,
                        left_sum + solve(left, mid),
                        right_sum + solve(mid + 1, right)
                    )

            dp[left][right] = ans
            return ans

        return solve(0, n - 1)