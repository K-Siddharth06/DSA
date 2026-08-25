class Solution(object):
    def reverseWords(self, s):
        n = len(s)
        words = []
        i = 0

        while i < n:
            while i < n and s[i] == ' ':
                i += 1

            if i >= n:
                break

            j = i
            while j < n and s[j] != ' ':
                j += 1

            words.append(s[i:j])
            i = j

        ans = ""
        i = len(words) - 1

        while i >= 0:
            ans += words[i]
            if i != 0:
                ans += " "
            i -= 1

        return ans