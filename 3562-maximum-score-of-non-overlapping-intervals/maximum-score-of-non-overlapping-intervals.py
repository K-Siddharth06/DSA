from bisect import bisect_right

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in a]

        dp = [[(0, ()) for _ in xrange(5)] for _ in xrange(n + 1)]

        for i in xrange(n - 1, -1, -1):
            l, r, w, idx = a[i]
            nxt = bisect_right(starts, r, i + 1)

            for k in xrange(1, 5):
                best = dp[i + 1][k]

                score = w + dp[nxt][k - 1][0]
                ids = tuple(sorted((idx,) + dp[nxt][k - 1][1]))

                if score > best[0] or (score == best[0] and ids < best[1]):
                    best = (score, ids)

                dp[i][k] = best

        return list(dp[0][4][1])