class Solution(object):
    def maxProduct(self, nums):
        i=0
        maxend=nums[0]
        minend=nums[0]
        res=nums[0]
        n=len(nums)
        for i in range(1,n):
            v1=nums[i]
            v2=nums[i]*maxend
            v3=nums[i]*minend
            maxend=max(v1,max(v2,v3))
            minend=min(v1,min(v2,v3))
            res=max(res,max(maxend,minend))
        return res

        