# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mx = 0
        self.ans = True
        self.con = []
    
    def determineLevel(self, root, lvl):
        if not root:
            return
        
        self.mx = max(self.mx, lvl)
        
        self.determineLevel(root.left, lvl + 1)
        self.determineLevel(root.right, lvl + 1)
    
    def solve(self, root, lvl):
        if not root:
            return
        
        if lvl < self.mx - 1 and (not root.left or not root.right):
            self.ans = False
            return
        
        if lvl == self.mx - 1:
            self.con.append(root.left)
            self.con.append(root.right)
        
        self.solve(root.left, lvl + 1)
        self.solve(root.right, lvl + 1)
        
    def isCompleteTree(self, root: TreeNode) -> bool:
        self.determineLevel(root, 0)
        self.solve(root, 0)
        
        while len(self.con) and not self.con[-1]:
            self.con.pop()
            
        if None in self.con:
            return False
        
        return self.ans
