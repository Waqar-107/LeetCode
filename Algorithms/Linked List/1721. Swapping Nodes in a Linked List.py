# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = None
        second = None
        length = 0
        
        idx = 1
        temp = head
        while temp:
            if idx == k:
                first = temp
            
            idx += 1
            temp = temp.next
            length += 1
        
        idx = 1
        temp = head
        while temp:
            if length - k + 1 == idx:
                second = temp
            
            idx += 1
            temp = temp.next
        
        first.val, second.val = second.val, first.val
        
        return head
