# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return
        tempA = headA
        tempB = headB
        while tempA and tempB:
            tempA = tempA.next
            tempB = tempB.next
        
        if not tempA:
            tempA = headB
            while tempA:
                if not tempB:
                    tempB = headA
                if tempA == tempB:
                    return tempA
                tempB = tempB.next
                tempA = tempA.next
        
        if not tempB:
            tempB = headA
            while tempB:
                if not tempA:
                    tempA = headB
                if tempA == tempB:
                    return tempA
                tempB = tempB.next
                tempA = tempA.next
        