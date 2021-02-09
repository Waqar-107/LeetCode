# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cnt = 0
        
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        
        idx = 1
        cnt = cnt // 2 + 1
        
        temp = head
        while temp:
            if idx == cnt:
                return temp
            
            idx += 1
            temp = temp.next
        
        return None
            
