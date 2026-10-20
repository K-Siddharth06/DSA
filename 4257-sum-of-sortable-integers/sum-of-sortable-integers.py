class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0
        divisors = []
        i = 1

        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1

        for k in divisors:
            valid = True
            prev = None

            start = 0
            while start < n and valid:
                mn = nums[start]
                mx = nums[start]
                desc = 0
                j = start

                while j < start + k:
                    if nums[j] < mn:
                        mn = nums[j]
                    if nums[j] > mx:
                        mx = nums[j]
                    nxt = start + (j - start + 1) % k
                    if nums[j] > nums[nxt]:
                        desc += 1
                    j += 1

                if desc > 1:
                    valid = False
                    break

                if prev is not None and prev > mn:
                    valid = False
                    break

                prev = mx
                start += k

            if valid:
                ans += k

        return ans