# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        res = 0

        def dfs(node):
            if not node:
                return
            nonlocal n, res
            if n == k:
                return
            dfs(node.left)
            n+=1 
            if n == k:
                res = node.val
                return 
            dfs(node.right)
        
        dfs(root)
        return res

