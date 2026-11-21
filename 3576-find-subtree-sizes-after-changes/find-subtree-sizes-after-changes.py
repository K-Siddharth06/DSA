class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in xrange(n)]

        for i in xrange(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26

        def find_parents(node):
            c = ord(s[node]) - ord('a')
            old = last[c]

            if old != -1:
                new_parent[node] = old

            last[c] = node

            for child in children[node]:
                find_parents(child)

            last[c] = old

        find_parents(0)

        new_children = [[] for _ in xrange(n)]

        for i in xrange(1, n):
            new_children[new_parent[i]].append(i)

        ans = [0] * n

        def dfs(node):
            size = 1

            for child in new_children[node]:
                size += dfs(child)

            ans[node] = size
            return size

        dfs(0)
        return ans