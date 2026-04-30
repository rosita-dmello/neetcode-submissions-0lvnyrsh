# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
     

        def traverse(root, res):
            if not root:
                return

            left = traverse(root.left, res)
            res.append(root.val)
            right = traverse(root.right, res)

            return res

        traverse(root,res)
        return res