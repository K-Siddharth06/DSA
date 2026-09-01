from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])
        litter = {}
        start = None
        k = 0

        for i in xrange(m):
            for j in xrange(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        full = (1 << k) - 1
        q = deque()
        q.append((start[0], start[1], energy, 0, 0))

        seen = {}

        while q:
            r, c, e, mask, d = q.popleft()

            if mask == full:
                return d

            key = (r, c, mask)

            if key in seen and seen[key] >= e:
                continue

            seen[key] = e

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X' or e == 0:
                    continue

                ne = e - 1
                nm = mask

                if (nr, nc) in litter:
                    nm |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                q.append((nr, nc, ne, nm, d + 1))

        return -1