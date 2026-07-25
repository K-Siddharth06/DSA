class Solution(object):
    def twoSum(self, nums, target):
        i=0
        seen={}
        while i<len(nums):
            needed=target-nums[i]
            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]]=i
            i=i+1
        return []
        