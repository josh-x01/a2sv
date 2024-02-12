# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return -1 
        f = s = head
        while f and f.next and f.next.next:
            f = f.next.next
            s = s.next
        else:
            if f.next:
                s = s.next
        return s