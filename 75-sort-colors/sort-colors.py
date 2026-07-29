class Solution(object):
    def sortColors(self, nums):
        zero = 0
        one = 0
        two = 0

        # Count the occurrences
        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            else:
                two += 1

        # Fill the array with 0s
        i = 0
        while zero > 0:
            nums[i] = 0
            i += 1
            zero -= 1

        # Fill the array with 1s
        while one > 0:
            nums[i] = 1
            i += 1
            one -= 1

        # Fill the array with 2s
        while two > 0:
            nums[i] = 2
            i += 1
            two -= 1