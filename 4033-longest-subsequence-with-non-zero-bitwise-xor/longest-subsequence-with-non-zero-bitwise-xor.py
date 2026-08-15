class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)
        xor = 0
        has_nonzero = False

        for x in nums:
            xor ^= x

            if x != 0:
                has_nonzero = True

        if xor != 0:
            return n

        if has_nonzero:
            return n - 1

        return 0