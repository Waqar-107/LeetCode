# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = None
        idx = 0
        after = None
        
        temp = list1
        while temp:
            if idx == a - 1:
                prev = temp
            
            if idx == b + 1:
                after = temp
                
            temp = temp.next
            idx += 1
        
        temp = list2
        while temp.next:
            temp = temp.next
        
        if prev:
            prev.next = list2
            temp.next = after
            
            return list1
        
        else:
            temp.next = after
            return list2
