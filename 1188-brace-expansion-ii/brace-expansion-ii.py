class Solution(object):
    def braceExpansionII(self, expression):
        def parse(i):
            res = set()
            cur = set([''])

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    res |= cur
                    cur = set([''])
                    i += 1
                elif expression[i] == '{':
                    sub, i = parse(i + 1)
                    cur = set(a + b for a in cur for b in sub)
                else:
                    cur = set(a + expression[i] for a in cur)
                    i += 1

            res |= cur
            return res, i + 1

        return sorted(parse(0)[0])