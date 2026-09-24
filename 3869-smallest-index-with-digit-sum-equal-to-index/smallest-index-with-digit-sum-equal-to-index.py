class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            n = nums[i]
            total = 0

            while n > 0:
                total += n % 10
                n //= 10

            if total == i:
                return i

        return -1