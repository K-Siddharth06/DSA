from fractions import gcd

class Solution(object):
    def maxLength(self, nums):
        n = len(nums)
        ans = 0

        for i in xrange(n):
            prod = 1
            g = 0
            l = 1

            for j in xrange(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans