class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i in xrange(len(s)):
            value = 26 - (ord(s[i]) - ord('a'))
            ans += value * (i + 1)

        return ans