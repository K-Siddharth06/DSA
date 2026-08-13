class Solution(object):
    def removeElements(self, head, val):
        temp = ListNode(0)
        temp.next = head
        curr = temp
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return temp.next
