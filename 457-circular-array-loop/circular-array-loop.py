class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i, forward):
            if nums[i] == 0 or (nums[i] > 0) != forward:
                return -1
            j = (i + nums[i]) % n
            if j == i:
                return -1
            return j

        for i in range(n):
            if nums[i] == 0:
                continue

            forward = nums[i] > 0
            slow = i
            fast = i

            while True:
                slow = next_index(slow, forward)
                if slow == -1:
                    break

                fast = next_index(fast, forward)
                if fast == -1:
                    break

                fast = next_index(fast, forward)
                if fast == -1:
                    break

                if slow == fast:
                    return True

            j = i
            while nums[j] != 0 and (nums[j] > 0) == forward:
                nxt = (j + nums[j]) % n
                nums[j] = 0
                j = nxt

        return False