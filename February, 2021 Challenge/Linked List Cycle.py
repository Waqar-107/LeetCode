# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return head
        
        hare = head
        tortoise = head
        
        while hare.next and hare.next.next and tortoise.next:
            hare = hare.next.next   
            tortoise = tortoise.next
            
            if hare == tortoise:
                tortoise = head
                while hare != tortoise:
                    hare = hare.next
                    tortoise = tortoise.next
                
                return hare
            
        return None
        
        
