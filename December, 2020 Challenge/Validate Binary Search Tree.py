# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.last = None
        self.ans = True
    
    def solve(self, root):
        if not root:
            return
        
        self.solve(root.left)
        
        if self.last and self.last.val >= root.val:
            self.ans = False
            return
        self.last = root
        
        self.solve(root.right)
        
    def isValidBST(self, root: TreeNode) -> bool:
        self.solve(root)
        return self.ans
