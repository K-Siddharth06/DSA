class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        even = 1
        odd = 0
        ans = 0
        parity = 0

        for num in arr:
            parity ^= num & 1

            if parity == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1

        return ans % MOD