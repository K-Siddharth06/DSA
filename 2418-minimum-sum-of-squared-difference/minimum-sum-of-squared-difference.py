class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        lo, hi = 0, max(diffs)

        while lo < hi:
            mid = (lo + hi) // 2
            if sum(max(0, d - mid) for d in diffs) > k:
                lo = mid + 1
            else:
                hi = mid

        ans = sum(min(d, lo) ** 2 for d in diffs)
        remaining = k - sum(max(0, d - lo) for d in diffs)

        return ans - remaining * (2 * lo - 1)