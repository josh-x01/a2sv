# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        length = 1
        temp = head
        tail = None
        while temp.next:
            temp = temp.next
            length += 1
        else:
            tail = temp
        k = k % length
        temp = head
        for i in range(length - k -1):
            temp = temp.next
        tail.next = head
        head = temp.next
        temp.next = None
        
        return head

        