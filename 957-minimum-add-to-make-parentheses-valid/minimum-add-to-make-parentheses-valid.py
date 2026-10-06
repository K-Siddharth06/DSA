class Solution(object):
    def minAddToMakeValid(self, s):
        open_count = 0
        ans = 0

        for ch in s:
            if ch == '(':
                open_count += 1
            elif open_count:
                open_count -= 1
            else:
                ans += 1

        return ans + open_count