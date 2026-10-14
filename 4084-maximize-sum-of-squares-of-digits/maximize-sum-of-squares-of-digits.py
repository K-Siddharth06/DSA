class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        q, r = divmod(sum, 9)
        ans = '9' * q

        if r:
            ans += str(r)

        ans += '0' * (num - len(ans))
        return ans