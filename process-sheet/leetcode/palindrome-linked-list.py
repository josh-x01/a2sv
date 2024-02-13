# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        store = []
        temp = head
        while temp.next:
            store.append(temp)
            temp = temp.next
        store.append(temp)
        length = len(store)
        l = length//2 - 1
        r = math.ceil(length/2)
        for i in range(length//2):
            if store[l].val != store[r].val:
                return False
            l -= 1
            r += 1
        return True