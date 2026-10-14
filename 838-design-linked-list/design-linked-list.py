class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None

class MyLinkedList(object):

    def __init__(self):
        self.temp=Node()
        self.size=0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        curr=self.temp
        for i in range(index+1):
            curr=curr.next
        return curr.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node=Node(val)
        new_node.next=self.temp.next
        self.temp.next=new_node
        self.size+=1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        curr=self.temp
        while curr.next:
            curr=curr.next
        curr.next=Node(val)
        self.size+=1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index>self.size:
            return None
        if index<0:
            index=0
        
        curr=self.temp
        for i in range(index):
            curr=curr.next
        new_node=Node(val)
        new_node.next=curr.next
        curr.next=new_node
        self.size+=1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:
            return None
        curr=self.temp
        for i in range(index):
            curr=curr.next
        curr.next=curr.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)