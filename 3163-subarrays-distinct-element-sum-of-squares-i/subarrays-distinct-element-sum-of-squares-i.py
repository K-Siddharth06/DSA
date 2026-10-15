class Solution(object):
    def sumCounts(self, nums):
        n = len(nums)
        ans = 0
        i = 0
        while i < n:
            seen = set()
            j = i
            while j < n:
                seen.add(nums[j])
                d = len(seen)
                ans += d * d
                j += 1
            i += 1
        return ans