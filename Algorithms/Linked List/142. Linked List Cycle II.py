# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise = head
        hare = head
        
        while hare and hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next
            
            if hare == tortoise:
                tortoise = head
                while hare != tortoise:
                    hare = hare.next
                    tortoise = tortoise.next
                
                return hare
        
        return None