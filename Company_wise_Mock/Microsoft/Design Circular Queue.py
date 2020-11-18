class MyCircularQueue:

    def __init__(self, k: int):
        self.container = [0] * k
        self.first = 0  
        self.ins = 0
        self.sz = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.container[self.ins] = value
        self.ins = (self.ins + 1) % len(self.container)
        self.sz += 1
        
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.first = (self.first + 1) % len(self.container)
        self.sz -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.container[self.first]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        if self.ins == 0:
            return self.container[-1]
        
        return self.container[self.ins - 1]
        

    def isEmpty(self) -> bool:
        return self.sz == 0
        

    def isFull(self) -> bool:
        return self.sz == len(self.container)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
