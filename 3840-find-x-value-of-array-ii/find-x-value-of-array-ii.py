class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        for i in range(n):
            x = nums[i] % k
            prod[size + i] = x
            cnt[size + i][x] = 1

        for i in range(size - 1, 0, -1):
            lp = prod[2 * i]
            rp = prod[2 * i + 1]
            prod[i] = (lp * rp) % k

            cur = cnt[i]
            left = cnt[2 * i]
            right = cnt[2 * i + 1]

            for r in range(k):
                cur[r] = left[r]

            for r in range(k):
                cur[(lp * r) % k] += right[r]

        def update(pos, value):
            p = size + pos
            x = value % k

            prod[p] = x
            cnt[p] = [0] * k
            cnt[p][x] = 1

            p //= 2

            while p:
                lp = prod[2 * p]
                rp = prod[2 * p + 1]

                prod[p] = (lp * rp) % k

                cur = [0] * k
                left = cnt[2 * p]
                right = cnt[2 * p + 1]

                for r in range(k):
                    cur[r] = left[r]

                for r in range(k):
                    cur[(lp * r) % k] += right[r]

                cnt[p] = cur
                p //= 2

        def merge(a, b):
            ap, ac = a
            bp, bc = b

            res = ac[:]

            for r in range(k):
                res[(ap * r) % k] += bc[r]

            return (ap * bp % k, res)

        def query(l, r):
            l += size
            r += size

            left_nodes = []
            right_nodes = []

            while l <= r:
                if l & 1:
                    left_nodes.append(l)
                    l += 1

                if not (r & 1):
                    right_nodes.append(r)
                    r -= 1

                l //= 2
                r //= 2

            nodes = left_nodes + right_nodes[::-1]

            current = (1, [0] * k)

            for node in nodes:
                current = merge(current, (prod[node], cnt[node]))

            return current[1]

        ans = []

        for index, value, start, x in queries:
            update(index, value)
            counts = query(start, n - 1)
            ans.append(counts[x])

        return ans