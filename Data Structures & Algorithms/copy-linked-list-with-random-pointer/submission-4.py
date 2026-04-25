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
        #2 pass interleaved

        if not head:
            return None
        curr1 = head

        while curr1:
            tmp = curr1.next
            new_node = Node(curr1.val, tmp)
            curr1.next = new_node
            curr1 = tmp
        
        curr1 = head
        curr2 = head.next

        while curr1:
            if curr1.random:
                curr2.random = curr1.random.next
            curr1 = curr2.next
            if curr2.next:
                curr2 = curr2.next.next 
        curr1 = head
        curr2 = new_head = head.next

        while curr1:
            curr1.next = curr1.next.next
            if curr2.next:
                curr2.next = curr2.next.next
            curr1 = curr1.next
            curr2 = curr2.next
            
        return new_head

        