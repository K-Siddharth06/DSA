class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = ListNode(0)
        cur = dummy

        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        if left:
            cur.next = left
        else:
            cur.next = right

        return dummy.next