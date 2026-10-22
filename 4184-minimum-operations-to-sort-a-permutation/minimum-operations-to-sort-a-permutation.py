class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        z = 0

        while nums[z] != 0:
            z += 1

        ans = -1
        ok = True
        i = 0

        while i < n:
            if nums[(z + i) % n] != i:
                ok = False
                break
            i += 1

        if ok:
            ans = z
            if n - z + 2 < ans:
                ans = n - z + 2

        k = (n - 1 - z) % n
        ok = True
        i = 0

        while i < n:
            if nums[n - 1 - ((i + k) % n)] != i:
                ok = False
                break
            i += 1

        if ok:
            cost = 1 + k
            if n - k + 1 < cost:
                cost = n - k + 1
            if ans == -1 or cost < ans:
                ans = cost

        return ans