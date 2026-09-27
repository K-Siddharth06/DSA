class Solution:
    def reverseParentheses(self, s):
        stack = []
        cur = []

        for ch in s:
            if ch == '(':
                stack.append(cur)
                cur = []
            elif ch == ')':
                cur.reverse()
                cur = stack.pop() + cur
            else:
                cur.append(ch)

        return ''.join(cur)