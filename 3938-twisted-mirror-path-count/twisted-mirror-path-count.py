class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in xrange(m)]
        dp[0][0] = 1

        for i in xrange(m):
            for j in xrange(n):
                ways = dp[i][j]
                if ways == 0 or (i == m - 1 and j == n - 1):
                    continue

                for di, dj in ((0, 1), (1, 0)):
                    r, c = i + di, j + dj

                    while 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        if di == 0:
                            r += 1
                            di, dj = 1, 0
                        else:
                            c += 1
                            di, dj = 0, 1

                    if 0 <= r < m and 0 <= c < n:
                        dp[r][c] = (dp[r][c] + ways) % MOD

        return dp[m - 1][n - 1]