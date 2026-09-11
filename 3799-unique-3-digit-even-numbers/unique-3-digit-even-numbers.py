class Solution(object):
    def totalNumbers(self, digits):
        ans = set()
        n = len(digits)

        for i in xrange(n):
            for j in xrange(n):
                for k in xrange(n):
                    if i != j and i != k and j != k:
                        if digits[i] != 0 and digits[k] % 2 == 0:
                            ans.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        return len(ans)