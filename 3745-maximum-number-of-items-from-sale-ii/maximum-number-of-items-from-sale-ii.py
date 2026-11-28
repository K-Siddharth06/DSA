class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1
        M = [0] * (n + 1)
        for f in range(1, n + 1):
            s = 0
            for m in range(f, n + 1, f):
                s += cnt[m]
            M[f] = s
        pmin = min(p for _, p in items)
        cand = sorted((p, M[f] - 1) for f, p in items if p < 2 * pmin and M[f] > 1)
        R = budget
        res = 0
        for p, d in cand:
            t = min(d, R // p)
            res += 2 * t
            R -= t * p
            if t < d:
                break
        return res + R // pmin
        
        