class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        if k == n:
            return max(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        if k == 1:
            ans = -1
            for x in nums:
                if freq[x] == 1:
                    ans = max(ans, x)
            return ans
        ans = -1
        if freq[nums[0]] == 1:
            ans = max(ans, nums[0])
        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])
        return ans