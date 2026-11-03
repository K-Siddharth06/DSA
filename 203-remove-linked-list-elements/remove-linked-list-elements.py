class Solution(object):
    def removeElements(self, head, val):
        temp=ListNode(0)
        temp.next=head
        cur=temp
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return temp.next
        