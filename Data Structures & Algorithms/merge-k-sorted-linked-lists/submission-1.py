# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def divide(self, lists, l, r):
        if l == r:
            return lists[l]
        if l > r:
            return None

        mid = l + (r-l)//2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid+1, r)

        return self.conquer(left, right)

    def conquer(self, left, right):
        l = left
        r = right
        dummy = c = ListNode()
        while l and r:
            if l.val < r.val:
                c.next = l
                l = l.next
            else:
                c.next = r
                r = r.next
            c = c.next

        c.next = l or r

        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        return self.divide(lists, 0, len(lists) - 1)
