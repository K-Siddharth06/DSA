class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum=nums[0]
        min_sum=nums[0]
        cur_max=nums[0]
        cur_min=nums[0]
        for i in nums[1:]:
            cur_max=max(i,cur_max+i)
            cur_min=min(i,cur_min+i)
            max_sum=max(max_sum,cur_max)
            min_sum=min(min_sum,cur_min)
        return max(max_sum,abs(min_sum))    
