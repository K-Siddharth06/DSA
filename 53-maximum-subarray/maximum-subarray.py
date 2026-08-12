class Solution(object):
    def maxSubArray(self, nums):
        i=0
        best_ending=nums[0]
        ans=nums[0]
        n=len(nums)
        for i in range(1,n):
            v1=best_ending+nums[i]
            v2=nums[i]
            best_ending=max(v1,v2)
            ans=max(ans,best_ending)
        return ans