class Solution:
    def removeNthFromEnd(self, head, n):
        temp = ListNode(0)
        temp.next = head
        slow = temp
        fast = temp

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return temp.next