class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for ch in s1:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        k = len(s1)

        for i in range(k):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1

        if window == need:
            return True

        for i in range(k, len(s2)):

            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1

            window[s2[i - k]] -= 1

            if window[s2[i - k]] == 0:
                del window[s2[i - k]]

            if window == need:
                return True

        return False