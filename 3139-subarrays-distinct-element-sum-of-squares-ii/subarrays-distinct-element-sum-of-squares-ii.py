class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        s = [0] * (4 * n)
        q = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                length = r - l + 1
                v = lazy[node] + 1
                q[node] = (q[node] + 2 * s[node] + length) % MOD
                s[node] = (s[node] + length) % MOD
                lazy[node] += 1
                return

            mid = (l + r) // 2
            a = node * 2
            b = a + 1

            if lazy[node]:
                v = lazy[node]
                left_len = mid - l + 1
                right_len = r - mid

                q[a] = (q[a] + 2 * v * s[a] + left_len * v * v) % MOD
                q[b] = (q[b] + 2 * v * s[b] + right_len * v * v) % MOD
                s[a] = (s[a] + left_len * v) % MOD
                s[b] = (s[b] + right_len * v) % MOD
                lazy[a] += v
                lazy[b] += v
                lazy[node] = 0

            if ql <= mid:
                update(a, l, mid, ql, qr)
            if qr > mid:
                update(b, mid + 1, r, ql, qr)

            s[node] = (s[a] + s[b]) % MOD
            q[node] = (q[a] + q[b]) % MOD

        i = 0
        while i < n:
            p = last.get(nums[i], -1) + 1
            update(1, 0, n - 1, p, i)
            ans = (ans + q[1]) % MOD
            last[nums[i]] = i
            i += 1

        return ans