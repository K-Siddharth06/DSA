class Solution(object):
    def averageOfSubtree(self, root):
        ans = [0]

        def dfs(node):
            if not node:
                return 0, 0

            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)

            total = ls + rs + node.val
            count = lc + rc + 1

            if total / count == node.val:
                ans[0] += 1

            return total, count

        dfs(root)
        return ans[0]