def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum = curr_sum * 10 + node.val

            if not node.left and not node.right:
                return curr_sum

            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)

        return dfs(root, 0)