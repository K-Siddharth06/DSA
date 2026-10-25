class Solution(object):
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 1:
                return

            grid[r][c] = 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in xrange(m):
            dfs(r, 0)
            dfs(r, n - 1)

        for c in xrange(n):
            dfs(0, c)
            dfs(m - 1, c)

        ans = 0

        for r in xrange(1, m - 1):
            for c in xrange(1, n - 1):
                if grid[r][c] == 0:
                    ans += 1
                    dfs(r, c)

        return ans