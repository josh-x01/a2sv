# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head
        while temp.next and temp.next.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
                continue
            temp = temp.next
        else:
            if temp.val == temp.next.val:
                temp.next = None
        return head
        