# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        stack = [[p, q]]
        
        while stack:
            pn, qn = stack.pop()
            if pn and qn:
                if pn.val != qn.val:
                    same = False
                    break
                stack.append([pn.left, qn.left])
                stack.append([pn.right, qn.right])
            else:
                if pn != qn:
                    same = False
                    break
        return same
            


            