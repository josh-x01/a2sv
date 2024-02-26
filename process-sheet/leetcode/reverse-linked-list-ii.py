# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_head = ListNode()
        new_head.next = head
        left_node = right_node = prev = new_head
        right += 1
        while right:
            if left:
                left_node = left_node.next
                left -=1
                if left:
                    prev = prev.next
            right_node = right_node.next
            right -= 1
        start = left_node
        last_node = right_node
        while start != last_node:
            hold = start.next
            start.next = right_node
            right_node = start
            start = hold
        prev.next = right_node

        return new_head.next