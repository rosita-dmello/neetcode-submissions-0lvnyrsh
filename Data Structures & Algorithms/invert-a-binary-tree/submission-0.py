class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if not node:
                return

            left = invert(node.left)
            right = invert(node.right)
            node.left, node.right = node.right, node.left
        invert(root)

        return root