# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        l = r = head
        hasCycle = False
        while r.next and r.next.next:
            l = l.next
            r = r.next.next
            if l == r:
                hasCycle = True
                break
        if not hasCycle:
            return
        l = head
        while r.next:
            if l == r:
                return l
            l = l.next
            r = r.next
