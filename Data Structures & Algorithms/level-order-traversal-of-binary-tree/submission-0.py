# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            q_len = len(q)
            sub_q = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    sub_q.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if sub_q:
                res.append(sub_q)
        return res
