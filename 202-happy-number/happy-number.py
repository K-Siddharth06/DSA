class Solution(object):
    def isHappy(self, n):
        def get_sum(n):
            total=0
            while n>0:
                digit=n%10
                n=n//10
                total+=digit*digit
            return total
        slow=n
        fast=n
        while fast!=1:
            slow=get_sum(slow)
            fast=get_sum(get_sum(fast))
            if slow==fast and slow!=1:
                return False
        return True
        