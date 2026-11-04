class Solution:
    def reverseList(self, head):
        prev=None
        cur=head
        while cur:
            first_node=cur.next
            cur.next=prev
            prev=cur
            cur=first_node
        return prev
