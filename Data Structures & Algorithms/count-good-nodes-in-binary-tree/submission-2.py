# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# bfs
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append((root, root.val))
        res = 0

        while q:
            for i in range(len(q)):
                node, maxVal = q.popleft()
                if node:
                    if node.val >= maxVal:
                        res += 1
                    maxVal = max(node.val, maxVal)
                    q.append((node.left, maxVal))
                    q.append((node.right, maxVal))
            
        return res
