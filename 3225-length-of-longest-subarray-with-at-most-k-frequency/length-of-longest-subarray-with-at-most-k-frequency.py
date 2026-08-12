class Solution(object):
    def maxSubarrayLength(self, nums, k):
        freq = {}
        low = 0
        ans = 0
        for high in range(len(nums)):
            if nums[high] in freq:
                freq[nums[high]] += 1
            else:
                freq[nums[high]] = 1

            while freq[nums[high]] > k:
                freq[nums[low]] -= 1
                low += 1
            length = high - low + 1
            if length > ans:
                ans = length
        return ans