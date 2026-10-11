class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            end = prev

            for _ in xrange(k):
                end = end.next
                if not end:
                    return dummy.next

            start = prev.next
            nxt = end.next

            prev.next = None
            end.next = None

            curr = start
            last = None

            while curr:
                temp = curr.next
                curr.next = last
                last = curr
                curr = temp

            prev.next = last
            start.next = nxt
            prev = start