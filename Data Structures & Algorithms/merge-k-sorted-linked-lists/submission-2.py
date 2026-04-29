class Solution:
    def merge(self, left, right):
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
        if not lists:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]