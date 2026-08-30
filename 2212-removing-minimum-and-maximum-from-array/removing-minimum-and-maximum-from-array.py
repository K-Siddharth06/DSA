class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        mn = 0
        mx = 0

        for i in xrange(n):
            if nums[i] < nums[mn]:
                mn = i
            if nums[i] > nums[mx]:
                mx = i

        if mn > mx:
            mn, mx = mx, mn

        return min(mx + 1, n - mn, mn + 1 + n - mx)