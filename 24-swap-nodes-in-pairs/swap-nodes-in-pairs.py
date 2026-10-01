class Solution:
    def swapPairs(self, head):
        temp = ListNode(0)
        temp.next = head

        prev = temp

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return temp.next