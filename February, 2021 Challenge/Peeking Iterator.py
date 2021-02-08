# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.hasPeeked = False
        self.iterator = iterator
        self.curr = None
        

    def peek(self):
        if not self.hasPeeked:
            self.curr = self.iterator.next()
            self.hasPeeked = True
        
        return self.curr
        

    def next(self):
        if not self.hasPeeked:
            self.curr = self.iterator.next()
        
        self.hasPeeked = False
        return self.curr
        

    def hasNext(self):
        if self.hasPeeked:
            return True
        
        return self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
