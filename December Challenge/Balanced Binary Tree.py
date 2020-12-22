# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
        
    def solve(self, root, level):
        if not root:
            return 0
        
        l = 0
        r = 0
        
        if root.left:
            l = self.solve(root.left, level + 1)
        
        if root.right:
            r = self.solve(root.right, level + 1)
        
        if abs(l - r) > 1:
            self.ans = False
        
        return max(l, r) + 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        self.solve(root, 1)
        return self.ans
    
