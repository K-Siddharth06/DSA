class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        a = []
        b = []

        for i in xrange(n):
            for j in xrange(n):
                if img1[i][j]:
                    a.append((i, j))
                if img2[i][j]:
                    b.append((i, j))

        count = {}
        ans = 0

        for x1, y1 in a:
            for x2, y2 in b:
                key = (x2 - x1, y2 - y1)
                count[key] = count.get(key, 0) + 1
                ans = max(ans, count[key])

        return ans