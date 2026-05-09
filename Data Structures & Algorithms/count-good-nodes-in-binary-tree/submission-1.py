# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#dfs - adding subtree results
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = root.val

        def dfs(node, maxVal):
            res = 0
            if not node:
                return 0
            
            if node.val >= maxVal:
                res = 1
            maxVal = max(maxVal, node.val)
            
            left_res = dfs(node.left, maxVal)
            right_res = dfs(node.right, maxVal)

            return res + left_res + right_res
        result = dfs(root, maxVal)

        return result
