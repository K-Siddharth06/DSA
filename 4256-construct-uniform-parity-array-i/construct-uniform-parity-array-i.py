class Solution(object):
    def uniformArray(self, nums1):
        odd = False
        even = False

        for x in nums1:
            if x % 2:
                odd = True
            else:
                even = True

        return True