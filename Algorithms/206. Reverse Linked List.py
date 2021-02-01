# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.ans = None
    
    def solve(self, root):
        if root.next == None:
            self.ans = root
            return root
        
        ret = self.solve(root.next)
        
        root.next = None
        ret.next = root
        
        return root
        
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        self.solve(head)
        return self.ans
