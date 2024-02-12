# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        temp = head
        l = r = temp
        while r.next and r.next.next:
            l = l.next
            r = r.next.next
            if l == r:
                return True
        return False