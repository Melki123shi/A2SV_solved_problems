class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        print(self.size, index + 1)

        current = self.head
        ind = index + 1
        while current.next != None and ind:
            current = current.next
            ind -= 1
            
        return current.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index == self.size:
            return  self.addAtTail(val) 
        if index == 0:
            return self.addAtHead(val)
        node = Node(val)
        ind = 0
        current = self.head
        prev = current
        while current.next != None and ind != index + 1:
            prev = current
            current = current.next
            ind += 1
        node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 

        ind = 0
        current = self.head
        prev = current
        while current.next != None and ind != index + 1:
            prev = current
            current = current.next
            ind += 1
        prev.next = current.next
        self.size -= 1

        

class Node:
    def __init__(self, value = None, next = None):
        self.val = value
        self.next = next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)