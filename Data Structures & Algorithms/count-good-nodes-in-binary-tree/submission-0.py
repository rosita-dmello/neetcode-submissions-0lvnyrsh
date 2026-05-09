# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#dfs
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        maxVal = root.val

        def dfs(node, maxVal):
            
            if not node:
                return
            
            if node.val >= maxVal:
                nonlocal res
                res += 1
            maxVal = max(maxVal, node.val)
            
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

            return
        dfs(root, maxVal)

        return res
