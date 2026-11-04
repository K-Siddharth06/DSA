class Solution(object):
    def numComponents(self, head, nums):
        values=set(nums)
        count=0
        cur=head
        while cur:
            if cur.val in values:
                if not cur.next or cur.next.val not in values:
                    count+=1
            cur=cur.next
        return count