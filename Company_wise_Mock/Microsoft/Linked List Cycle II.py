# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise = head
        hare = head
        
        while hare:
            tortoise = tortoise.next
            
            if not hare.next:
                return None
            
            hare = hare.next.next
            
            if hare == tortoise:
                tortoise = head
                while tortoise != hare:
                    tortoise = tortoise.next
                    hare = hare.next
                
                return hare
        
        return None
