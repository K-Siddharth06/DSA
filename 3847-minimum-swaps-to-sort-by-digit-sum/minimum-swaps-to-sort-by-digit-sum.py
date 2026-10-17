class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)
        arr = []

        for i in range(n):
            x = nums[i]
            s = 0
            while x:
                s += x % 10
                x //= 10
            arr.append((s, nums[i], i))

        arr.sort()
        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle += 1

            if cycle > 1:
                ans += cycle - 1

        return ans