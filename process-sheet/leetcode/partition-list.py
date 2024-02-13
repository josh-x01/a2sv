# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        gtlInit = ListNode(None)
        gtl = gtlInit
        lesInit = ListNode(None)
        les = lesInit
        temp = head
        while temp:
            if temp.val >= x:
                gtl.next = temp
                gtl = temp
                print('gtl', temp.val, end=' ')
                temp = temp.next
                gtl.next = None
            else:
                les.next = temp
                les = temp
                print('les', temp.val, end= ' ')
                temp = temp.next
                les.next = None
            print('out')
            # temp = temp.next
        # if gtlInit and les:
        les.next = gtlInit.next
        return lesInit.next
        
