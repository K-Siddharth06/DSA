# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        res=0
        cur=head
        while cur:
            res=res*2+cur.val
            cur=cur.next
        return res
        