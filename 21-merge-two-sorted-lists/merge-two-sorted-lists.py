class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp=ListNode(0)
        cur=temp
        while list1 and list2:
            if list1.val<=list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        if list1:
            cur.next=list1
        else:
            cur.next=list2
        return temp.next