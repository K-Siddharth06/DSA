
class Solution:
    def getDecimalValue(self, head):
        result=0
        cur=head
        while cur:
            result=result*2+cur.val
            cur=cur.next
        return result