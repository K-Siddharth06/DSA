class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        cnt = [0] * 26

        for i in xrange(len(s)):
            cnt[ord(s[i]) - 97] += 1
            cnt[ord(t[i]) - 97] -= 1

        return all(x == 0 for x in cnt)