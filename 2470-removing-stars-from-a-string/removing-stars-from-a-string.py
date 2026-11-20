class Solution(object):
    def removeStars(self, s):
        stack = ""

        for ch in s:
            if ch == '*':
                stack = stack[:-1]
            else:
                stack += ch

        return stack