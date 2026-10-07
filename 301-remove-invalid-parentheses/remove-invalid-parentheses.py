class Solution(object):
    def removeInvalidParentheses(self, s):
        def valid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        level = {s}

        while level:
            ans = []

            for x in level:
                if valid(x):
                    ans.append(x)

            if ans:
                return list(set(ans))

            next_level = set()

            for x in level:
                for i in xrange(len(x)):
                    if x[i] in '()':
                        next_level.add(x[:i] + x[i + 1:])

            level = next_level

        return ['']