# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(None, head)
        temp = dummy
        t1 = head.next
        t2 = head.next.next
        head.next = None
        t1.next = None
        while t2:
            while temp.next and t1.val > temp.next.val:
                temp = temp.next
            t1.next = temp.next
            temp.next = t1
            temp = dummy
            t1 = t2
            t2 = t2.next
        else:
            while temp.next and t1.val > temp.next.val:
                temp = temp.next
            t1.next = temp.next
            temp.next = t1
        head = dummy.next
        return head

      