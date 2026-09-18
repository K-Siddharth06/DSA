class Solution(object):
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i in xrange(n):
            x = ord(s[i]) - 97
            if first[x] == n:
                first[x] = i
            last[x] = i

        intervals = []

        for c in xrange(26):
            if first[c] == n:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - 97

                if first[x] < l:
                    valid = False
                    break

                if last[x] > r:
                    r = last[x]

                i += 1

            if valid:
                intervals.append((r, l))

        intervals.sort()

        ans = []
        end = -1

        for r, l in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans