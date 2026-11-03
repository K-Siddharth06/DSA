class Solution(object):
    def minMoves(self, nums):
        maximum = max(nums)
        return sum(maximum - num for num in nums)