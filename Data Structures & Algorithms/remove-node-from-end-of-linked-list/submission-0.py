# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0

        curr = head
        while curr:
            curr = curr.next
            N += 1 

        delete = N - n 

        if delete == 0:
            return head.next

        curr = head
        cnt = 0
        while curr:
            if cnt == delete - 1:
                curr.next = curr.next.next
                break
            cnt += 1
            curr = curr.next
        return head
            
