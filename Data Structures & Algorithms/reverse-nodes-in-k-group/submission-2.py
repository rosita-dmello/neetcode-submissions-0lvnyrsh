# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        kprev = dummy

        while True:
            curr = kprev
            for i in range(k):
                curr = curr.next
                if not curr:
                    break

            if not curr:
                break
            knext = curr.next
            prev = knext
            new_curr = group_head = kprev.next
            kprev.next = curr
            while new_curr != knext:
                tmp = new_curr.next
                new_curr.next = prev
                prev = new_curr
                new_curr = tmp
            kprev = group_head

        return dummy.next

