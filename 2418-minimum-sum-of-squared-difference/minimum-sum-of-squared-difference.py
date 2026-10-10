class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        freq = [0] * 100001

        for a, b in zip(nums1, nums2):
            freq[abs(a - b)] += 1

        for d in xrange(100000, 0, -1):
            if k <= 0:
                break

            take = min(k, freq[d])
            freq[d] -= take
            freq[d - 1] += take
            k -= take

        return sum(d * d * freq[d] for d in xrange(100001))