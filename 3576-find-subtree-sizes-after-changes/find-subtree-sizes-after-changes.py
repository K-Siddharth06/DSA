class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in xrange(n)]

        for i in xrange(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26
        prev = [-1] * n
        order = []
        stack = [0]

        while stack:
            node = stack.pop()

            if node < 0:
                node = ~node
                c = ord(s[node]) - 97
                last[c] = prev[node]
                continue

            c = ord(s[node]) - 97
            prev[node] = last[c]

            if last[c] != -1:
                parent[node] = last[c]

            last[c] = node
            order.append(node)

            stack.append(~node)

            for child in reversed(children[node]):
                stack.append(child)

        ans = [1] * n

        for node in reversed(order[1:]):
            ans[parent[node]] += ans[node]

        return ans