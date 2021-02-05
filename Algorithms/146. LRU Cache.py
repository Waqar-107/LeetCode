class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
        
class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.sz = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    # always insert in the head
    def add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node
            
    
    # remove a node
    def rem_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.key, end="->")
            temp = temp.next
        
        print()
    
    
    # takeout a node and place it in the head
    def move_order(self, node):
        self.rem_node(node)
        self.add_node(node)
        
    
    # if not found return -1
    # else, take the node out and place it in the head
    def get(self, key: int) -> int:
        if key in self.dict:
            self.move_order(self.dict[key])
            # self.print_list()
            return self.dict[key].value
        
        return -1
        
    
    # insert a node. if size exceeds capacity then delete from tail
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].value = value
            self.move_order(self.dict[key])
        
        else:
            node = Node(key, value)
            self.add_node(node)
            self.dict[key] = node
            self.sz += 1

            if self.sz > self.capacity:    
                del self.dict[self.tail.prev.key]
                self.rem_node(self.tail.prev)
                self.sz -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
