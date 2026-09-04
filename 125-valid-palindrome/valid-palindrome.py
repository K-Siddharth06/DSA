class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1

            while left < right and not self.isAlphaNum(s[right]):
                right -= 1

            if self.toLower(s[left]) != self.toLower(s[right]):
                return False

            left += 1
            right -= 1

        return True

    def isAlphaNum(self, c):
        return ('a' <= c <= 'z' or
                'A' <= c <= 'Z' or
                '0' <= c <= '9')

    def toLower(self, c):
        if 'A' <= c <= 'Z':
            return chr(ord(c) + 32)
        return c