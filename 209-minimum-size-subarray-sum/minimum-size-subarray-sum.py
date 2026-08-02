class Solution(object):
    def minSubArrayLen(self, target, nums):
        low=0
        high=0
        win_sum=0
        res=float('inf')
        n=len(nums)
        for high in range(n):
            win_sum=win_sum+nums[high]
            while win_sum>=target:
                cur_len=high-low+1
                res=min(res,cur_len)
                win_sum=win_sum-nums[low]
                low=low+1
        return 0 if res==float('inf') else res
