class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        left = 0
        ones = 0
        best = None

        for right in xrange(n):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                while s[left] == '0':
                    left += 1

                cur = s[left:right + 1]

                if best is None or len(cur) < len(best) or (len(cur) == len(best) and cur < best):
                    best = cur

        return best if best is not None else ""