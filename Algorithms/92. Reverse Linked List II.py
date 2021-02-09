# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.before = None
        self.after = None
        self.ans = None
    
    def solve(self, root, m, n, curr):
        if not root:
            return
        
        if curr < m:
            self.before = root
        if curr == n:
            self.after = root.next
            
            # if m > 1
            if self.before:
                self.before.next = root
            else:
                self.ans = root
        
        if root.next == None:
            return root
        
        ret = self.solve(root.next, m, n, curr + 1)
        
        if curr == m:
            root.next = self.after
            ret.next = root
        if curr > m and curr < n:
            ret.next = root
          
        return root
            
        
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        self.ans = head
        self.solve(head, m, n, 1)
        
        if self.before:
            return head
        else:
            return self.ans
        
