class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        from collections import deque

        graph = [[] for _ in xrange(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1
                pref[u] = (pref[p] if p != -1 else 0) ^ (1 << (ord(s[u]) - 97))

                stack.append((u, p, 1))
                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        LOG = n.bit_length()
        up = [parent[:]]
        for j in xrange(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in xrange(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit_idx = 0
            while diff:
                if diff & 1:
                    u = up[bit_idx][u]
                diff >>= 1
                bit_idx += 1

            if u == v:
                return u

            for j in xrange(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        bit = [0] * (n + 1)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def point_query(i):
            res = 0
            i += 1
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def update_subtree(u, delta):
            add(tin[u], delta)
            if tout[u] + 1 < n:
                add(tout[u] + 1, delta)

        chars = list(s)
        ans = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                delta = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97))
                update_subtree(u, delta)
                chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                pu = pref[u] ^ point_query(tin[u])
                pv = pref[v] ^ point_query(tin[v])
                mask = pu ^ pv ^ (1 << (ord(chars[w]) - 97))

                ans.append((mask & (mask - 1)) == 0)

        return ans