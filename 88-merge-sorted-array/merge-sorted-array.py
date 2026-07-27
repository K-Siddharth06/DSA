class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res = [0] * (m + n)
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            res[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            res[k] = nums2[j]
            j += 1
            k += 1
        for x in range(m + n):
            nums1[x] = res[x]