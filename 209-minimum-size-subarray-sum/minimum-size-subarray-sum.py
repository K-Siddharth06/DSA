class Solution(object):
    def minSubArrayLen(self, target, nums):
        low = 0
        win_sum = 0
        n = len(nums)
        res = float('inf')
        for high in range(n):
            win_sum += nums[high]
            while win_sum >= target:
                curr_len = high - low + 1
                res = min(res, curr_len)
                win_sum -= nums[low]
                low += 1
        return 0 if res == float('inf') else res