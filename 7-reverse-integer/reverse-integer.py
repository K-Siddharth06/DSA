class Solution(object):
    def reverse(self, x):
        sign = 1

        if x < 0:
            sign = -1
            x = -x

        ans = 0

        while x > 0:
            digit = x % 10
            ans = ans * 10 + digit
            x = x // 10

        ans = ans * sign

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans