# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        prev = None
        while node:
            if node.next == None:
                if prev:
                    prev.next = None
                
                break
                
            else:
                node.val = node.next.val
                prev = node
                node = node.next
                
                
        
