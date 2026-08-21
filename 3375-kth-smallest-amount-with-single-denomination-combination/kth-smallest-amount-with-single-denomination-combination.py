class Solution:
    def findKthSmallest(self, coins, k):

        n = len(coins)
        subsets = []

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    lcm = lcm // gcd(lcm, coins[i]) * coins[i]

            subsets.append((lcm, bits))

        def check(x):
            count = 0

            for lcm, bits in subsets:
                if bits % 2 == 1:
                    count += x // lcm
                else:
                    count -= x // lcm

            return count >= k

        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low