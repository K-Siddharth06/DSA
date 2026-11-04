class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}

        count = [0] * (m + 1)
        sums = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def kth(kth):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and count[nxt] < kth:
                    idx = nxt
                    kth -= count[nxt]
                step >>= 1

            return idx + 1

        def add(v, delta):
            i = rank[v]
            update(count, i, delta)
            update(sums, i, v * delta)

        def window_cost(total):
            mid = kth((x + 1) // 2)
            med = vals[mid - 1]
            left_count = query(count, mid)
            left_sum = query(sums, mid)

            return med * left_count - left_sum + (total - left_sum) - med * (x - left_count)

        for i in xrange(x):
            add(nums[i], 1)

        costs = [0] * (n - x + 1)
        total = sum(nums[:x])
        costs[0] = window_cost(total)

        for i in xrange(x, n):
            add(nums[i - x], -1)
            add(nums[i], 1)
            total += nums[i] - nums[i - x]
            costs[i - x + 1] = window_cost(total)

        prev = [0] * (n + 1)

        for t in xrange(1, k + 1):
            cur = [float('inf')] * (n + 1)

            for i in xrange(1, n + 1):
                cur[i] = cur[i - 1]

                if i >= x:
                    cur[i] = min(cur[i], prev[i - x] + costs[i - x])

            prev = cur

        return prev[n]