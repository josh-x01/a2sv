class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            newNode = Node(val)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
            self.size += 1                

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        newNode = Node(val)
        dummy = Node(None, self.head)
        temp = dummy
        for i in range(index):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        self.head = dummy.next
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        dummy = Node(None, self.head)
        temp = dummy
        
        for i in range(index):
            temp = temp.next
        temp.next = temp.next.next
        self.head = dummy.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)