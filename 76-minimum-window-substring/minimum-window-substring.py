class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = {}
        window = {}

        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        required = len(need)
        formed = 0

        low = 0
        minLen = float('inf')
        start = 0

        for high in range(len(s)):

            if s[high] in window:
                window[s[high]] += 1
            else:
                window[s[high]] = 1

            if s[high] in need and window[s[high]] == need[s[high]]:
                formed += 1

            while formed == required:

                if high - low + 1 < minLen:
                    minLen = high - low + 1
                    start = low

                window[s[low]] -= 1

                if s[low] in need and window[s[low]] < need[s[low]]:
                    formed -= 1

                low += 1

        if minLen == float('inf'):
            return ""

        return s[start:start + minLen]