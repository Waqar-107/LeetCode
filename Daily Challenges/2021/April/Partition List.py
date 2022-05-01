# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        arr = []
        
        temp = head
        while temp:
            if temp.val < x:
                arr.append(temp.val)
            
            temp = temp.next
        
        temp = head
        while temp:
            if temp.val >= x:
                arr.append(temp.val)
            
            temp = temp.next
            
        temp = head
        idx = 0
        while temp:
            temp.val = arr[idx]
            idx += 1
            temp = temp.next
        
        return head
