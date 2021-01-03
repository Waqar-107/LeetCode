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
    def __init__(self):
        self.levels = defaultdict(list)
        self.mx = 0
        
    def solve(self, root, level):
        if not root:
            return
        
        self.levels[level].append(root)
        self.mx = max(self.mx, level)
        
        self.solve(root.left, level + 1)
        self.solve(root.right, level + 1)
        
    def connect(self, root: 'Node') -> 'Node':
        self.solve(root, 0)
        for i in range(self.mx + 1):
            for j in range(len(self.levels[i]) - 1):
                self.levels[i][j].next = self.levels[i][j + 1]
                
        return root
