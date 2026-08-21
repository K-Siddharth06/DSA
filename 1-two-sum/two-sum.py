class Solution(object):
    def twoSum(self, nums, target):
        i=0
        seen={}
        while i<len(nums):
            need=target-nums[i]
            if need in seen:
              return [seen[need],i]
            seen[nums[i]]=i
            i=i+1
        return []
        