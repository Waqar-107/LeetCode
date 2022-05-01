# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        temp = head
        n = 0
        a = []
        
        while temp:
            a.append(temp.val)
            temp = temp.next
        
        a[k - 1], a[n - k] = a[n - k], a[k - 1]
        
        i = 0
        temp = head
        while temp:
            temp.val = a[i]
            i += 1
            temp = temp.next
        
        return head
