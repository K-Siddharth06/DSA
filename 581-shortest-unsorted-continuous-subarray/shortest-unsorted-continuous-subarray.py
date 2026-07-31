class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)

        left = -1
        right = -1

        max_seen = nums[0]

        for i in range(n):
            max_seen = max(max_seen, nums[i])

            if nums[i] < max_seen:
                right = i

        min_seen = nums[-1]

        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])

            if nums[i] > min_seen:
                left = i

        if right == -1:
            return 0

        return right - left + 1