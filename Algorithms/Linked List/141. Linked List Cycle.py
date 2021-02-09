# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        vis = {}
        while head:
            if head in vis:
                return True
            
            vis[head] = True
            head = head.next
        
        return False
        