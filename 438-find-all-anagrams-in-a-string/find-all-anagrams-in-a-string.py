class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        need = {}
        window = {}
        res = []

        for ch in p:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        k = len(p)

        for i in range(k):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1

        if window == need:
            res.append(0)

        for i in range(k, len(s)):

            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1

            window[s[i - k]] -= 1

            if window[s[i - k]] == 0:
                del window[s[i - k]]

            if window == need:
                res.append(i - k + 1)

        return res