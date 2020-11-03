# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = head
        parent = None
        
        while head:
            if head.next == None:
                break
            
            uno = head
            dos = head.next
            
            uno.next = dos.next
            dos.next = uno
            
            if parent:
                parent.next = dos
            else:
                root = dos
            
            parent = uno
            head = uno.next
        
        return root
