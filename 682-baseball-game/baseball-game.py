class Solution(object):
    def calPoints(self, operations):
        if operations is None:
            return 0
  
        stack = []
        sum1 = 0

        for char in operations:
            if char == '+':
                stack.append(int(stack[-1])+int(stack[-2]))
            elif char == 'D':
                t1 = int(stack.pop())
                stack.append(str(t1))
                stack.append(str(t1*2))
            elif char == 'C':
                stack.pop()
            else:
                stack.append(char)
        

        for i in stack:
            sum1 += int(i)
        return int(sum1)
        