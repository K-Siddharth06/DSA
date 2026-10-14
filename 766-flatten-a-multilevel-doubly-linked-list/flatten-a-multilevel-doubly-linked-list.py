"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):
        current = head
            
        while current:
            lastPart = current.next

            if current.child:
                child_end = current.child

                while child_end.next:
                    child_end = child_end.next
                
                current.next = current.child
                current.child.prev = current
                current.child = None

   
                if lastPart:
                    child_end.next = lastPart
                    lastPart.prev = child_end

            current = current.next
         
                    
        return head