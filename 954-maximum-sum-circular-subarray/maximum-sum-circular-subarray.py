class Solution(object):
    def maxSubarraySumCircular(self, nums):
        bestend=nums[0]
        ans=nums[0]
        worstend=nums[0]
        minans=nums[0]
        total=nums[0]
        for i in range(1,len(nums)):
            bestend=max(nums[i],bestend+nums[i])
            ans=max(ans,bestend)
            worstend=min(nums[i],worstend+nums[i])
            minans=min(minans,worstend)
            total=total+nums[i]
        if ans<0:
            return ans
        return max(ans,total-minans)
        