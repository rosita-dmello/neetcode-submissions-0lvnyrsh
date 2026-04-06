"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map_nodes = {None: None}

        curr = head

        while curr:
            map_nodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new = map_nodes[curr] 
            new.next = map_nodes[curr.next]
            new.random = map_nodes[curr.random]
            curr = curr.next

        return map_nodes[head]


        