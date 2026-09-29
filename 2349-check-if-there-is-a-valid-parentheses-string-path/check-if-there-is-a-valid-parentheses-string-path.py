class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [set() for _ in range(n)]
        dp[0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cur = set()

                if grid[i][j] == '(':
                    change = 1
                else:
                    change = -1

                if i > 0:
                    for balance in dp[j]:
                        new_balance = balance + change
                        if new_balance >= 0:
                            cur.add(new_balance)

                if j > 0:
                    for balance in dp[j - 1]:
                        new_balance = balance + change
                        if new_balance >= 0:
                            cur.add(new_balance)

                dp[j] = cur

        return 0 in dp[n - 1]