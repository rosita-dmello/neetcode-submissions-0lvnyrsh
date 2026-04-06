# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_ = set()
        curr = head

        while curr:
            if curr in set_:
                return True
            set_.add(curr)
            curr = curr.next
            
        return False