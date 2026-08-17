class Solution(object):
    def maxProduct(self, nums):
        i=0
        minend=nums[0]
        maxend=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            r1=nums[i]
            r2=minend*nums[i]
            r3=maxend*nums[i]
            minend=min(r1,min(r2,r3))
            maxend=max(r1,max(r2,r3))
            ans=max(ans,max(minend,maxend))
        return ans
       
