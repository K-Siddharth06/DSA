class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in xrange(n)]

        for i in xrange(n):
            for length in xrange(2, n - i + 1):
                best = INF

                for d in xrange(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    groups = length // d

                    for r in xrange(d):
                        for t in xrange(groups // 2):
                            a = i + r + t * d
                            b = i + r + (groups - 1 - t) * d

                            if s[a] != s[b]:
                                changes += 1

                    best = min(best, changes)

                cost[i][i + length - 1] = best

        dp = [[INF] * (n + 1) for _ in xrange(k + 1)]
        dp[0][0] = 0

        for parts in xrange(1, k + 1):
            for end in xrange(2 * parts, n + 1):
                for start in xrange(2 * (parts - 1), end - 1):
                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end - 1]
                    )

        return dp[k][n]