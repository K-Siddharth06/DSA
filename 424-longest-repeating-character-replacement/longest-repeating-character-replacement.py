class Solution(object):
    def characterReplacement(self, s, k):
        freq = {}
        low = 0
        maxFreq = 0
        res = 0

        for high in range(len(s)):
            if s[high] in freq:
                freq[s[high]] += 1
            else:
                freq[s[high]] = 1

            if freq[s[high]] > maxFreq:
                maxFreq = freq[s[high]]

            while (high - low + 1) - maxFreq > k:
                freq[s[low]] -= 1
                low += 1

            res = max(res, high - low + 1)

        return res