# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        a = head
        b = a.next
        p = None
        
        if b:
            ans = b
        else:
            return head
        
        while a and b:
            c = b.next
            a.next = c
            b.next = a
            
            if p:
                p.next = b
                
            p = a
            
            a = c
            
            if a:
                b = a.next
            else:
                b = None
        
        return ans
