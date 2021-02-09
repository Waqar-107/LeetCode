class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
        
class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    
    def print_list(self):
        temp = self.head
        
        while temp:
            print(temp.val, end = "=>")
            temp = temp.next
        
        print()

        
    def get(self, index: int) -> int:
        temp = self.head
        curr = -1  # start from -1 as we have a dummy head
        
        # even if index is equal to the dummy tail, it will return -1
        while temp:
            if curr == index:
                return temp.val
            
            temp = temp.next
            curr += 1
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        
        new_node.next = self.head.next
        new_node.prev = self.head
        
        self.head.next.prev = new_node
        self.head.next = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        prev = None
        curr = -1  # start from -1 as we have a dummy head
        
        # even if index is equal to the dummy tail, it will return -1
        while temp:
            # if temp.next is null then it is the dummy tail
            if curr == index - 1 and temp.next:
                prev = temp
                break
            
            temp = temp.next
            curr += 1
        
        if prev:
            new_node = Node(val)
            
            prev.next.prev = new_node
            new_node.next = prev.next
            
            prev.next = new_node
            new_node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        prev = None
        curr = -1  # start from -1 as we have a dummy head
        
        # even if index is equal to the dummy tail, it will return -1
        while temp:
            # if temp.next is null then it is the dummy tail
            if curr == index and temp.next:
                prev = temp.prev
                break
            
            temp = temp.next
            curr += 1
        
        if prev:
            prev.next.next.prev = prev
            prev.next = prev.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
