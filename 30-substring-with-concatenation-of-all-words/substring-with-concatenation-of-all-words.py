class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        wordLen = len(words[0])
        wordCount = len(words)
        totalLen = wordLen * wordCount

        need = {}

        for word in words:
            if word in need:
                need[word] += 1
            else:
                need[word] = 1

        res = []

        for offset in range(wordLen):

            low = offset
            window = {}
            count = 0

            for high in range(offset, len(s) - wordLen + 1, wordLen):

                word = s[high:high + wordLen]

                if word in need:

                    if word in window:
                        window[word] += 1
                    else:
                        window[word] = 1

                    count += 1

                    while window[word] > need[word]:
                        leftWord = s[low:low + wordLen]
                        window[leftWord] -= 1
                        low += wordLen
                        count -= 1

                    if count == wordCount:
                        res.append(low)

                        leftWord = s[low:low + wordLen]
                        window[leftWord] -= 1
                        low += wordLen
                        count -= 1

                else:
                    window = {}
                    count = 0
                    low = high + wordLen

        return res