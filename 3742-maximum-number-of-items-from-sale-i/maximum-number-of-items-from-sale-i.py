class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        items.sort(key=lambda x: x[1])

        factors = [x[0] for x in items]
        prices = [x[1] for x in items]

        free = [0] * n

        for i in xrange(n):
            for j in xrange(n):
                if i != j and factors[j] % factors[i] == 0:
                    free[i] += 1

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in xrange(n):
            cost = prices[i]
            value = 1 + free[i]

            for b in xrange(budget, cost - 1, -1):
                if dp[b - cost] != -1:
                    dp[b] = max(dp[b], dp[b - cost] + value)

        ans = 0

        for b in xrange(budget + 1):
            if dp[b] != -1:
                ans = max(ans, dp[b] + (budget - b) // prices[0])

        return ans