class Solution:
    def isPalindrome(self, head):

        arr = []  # Create an empty list to store node values

        while head:
            arr.append(head.val)  # Store each node's value
            head = head.next      # Move to the next node

        # Compare original list with its reverse
        return arr == arr[::-1]