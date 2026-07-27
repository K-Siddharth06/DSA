class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return res
               
        