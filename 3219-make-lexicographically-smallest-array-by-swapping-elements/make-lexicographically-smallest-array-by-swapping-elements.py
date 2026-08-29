class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        arr = []

        for i in xrange(n):
            arr.append((nums[i], i))

        arr.sort()

        ans = [0] * n
        i = 0

        while i < n:
            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            values = []
            indices = []

            k = i
            while k <= j:
                values.append(arr[k][0])
                indices.append(arr[k][1])
                k += 1

            indices.sort()

            k = 0
            while k < len(indices):
                ans[indices[k]] = values[k]
                k += 1

            i = j + 1

        return ans