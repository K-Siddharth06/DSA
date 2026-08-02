class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq = {}
        low = 0
        res = 0

        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high], 0) + 1

            while freq[s[high]] > 1:
                freq[s[low]] -= 1

                if freq[s[low]] == 0:
                    del freq[s[low]]

                low += 1

            length = high - low + 1
            res = max(res, length)

        return res