class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        unique=1
        j=1
        while j<len(nums):
            if nums[j]==nums[j-1]:
                j=j+1
                continue
            nums[i+1]=nums[j]
            i=i+1
            unique=unique+1
            j=j+1
        return unique
        
            
        
        