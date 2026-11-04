class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        current =  self.head
        current_index = 0
        while current and current_index<index:
            current = current.next
            current_index+=1
        return current.data if current else -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        
    def addAtTail(self, val: int) -> None:
        current = self.head
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return 
        while current.next:
            current = current.next
        current.next = newNode        

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        current = self.head
        current_index = 0
        while current and current_index<index-1:
            current = current.next
            current_index+=1

        if current is None:
            return 
        newNode = Node(val)
        newNode.next = current.next
        current.next = newNode
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index==0:
            
            self.head = self.head.next
            return 
        current = self.head
        current_index = 0
        while current and current_index<index-1:
            current = current.next
            current_index +=1
        if current is None or current.next is None:
            return 
        
        current.next = current.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)