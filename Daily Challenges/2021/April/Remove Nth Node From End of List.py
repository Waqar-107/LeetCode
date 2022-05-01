# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sz = 0
        
        temp = head
        while temp:
            sz += 1
            temp = temp.next
            
        if sz == n:
            head = head.next
            return head
        
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            
            if cnt == sz - n:
                temp.next = temp.next.next
                break
            
            temp = temp.next
        
        return head
