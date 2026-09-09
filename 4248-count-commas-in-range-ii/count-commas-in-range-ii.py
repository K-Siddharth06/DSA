class Solution(object):
    def countCommas(self, n):
        total = 0
        d = 1
        while True:
            lower = 1 if d == 1 else 10 ** (d - 1)
            if lower > n:
                break
            upper = min(n, 10 ** d - 1)
            cnt = upper - lower + 1
            total += cnt * ((d - 1) // 3)
            d += 1
        return total