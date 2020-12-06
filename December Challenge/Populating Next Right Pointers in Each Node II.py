"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def solve(self, root):
        if not root:
            return
        
        x = root.next
        
        # find the leftmost child f x
        while x:
            if x.left:
                x = x.left
                break
            if x.right:
                x = x.right
                break
            
            x = x.next
        
        if root.right:
            root.right.next = x
        if root.left:
            root.left.next = root.right if root.right else x
        
        self.solve(root.right)
        self.solve(root.left)
        
        return root
        
    def connect(self, root: 'Node') -> 'Node':
        return self.solve(root)
        
