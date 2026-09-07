class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 1000000007
        dp = [0] * 26
        total = 0

        for c in s:
            x = ord(c) - 97
            new = (total + 1) % MOD
            total = (total + new - dp[x]) % MOD
            dp[x] = new

        return total