# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.deepestLevel = 0
        self.ans = 0
    
    def findDeepestLevel(self, root, level):
        if not root:
            return
        
        self.deepestLevel = max(self.deepestLevel, level)
        
        self.findDeepestLevel(root.left, level + 1)
        self.findDeepestLevel(root.right, level + 1)
        
    def solve(self, root, level):
        if not root:
            return
        
        if level == self.deepestLevel:
            self.ans += root.val
        
        self.solve(root.left, level + 1)
        self.solve(root.right, level + 1)
        
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.findDeepestLevel(root, 0)
        self.solve(root, 0)
        
        return self.ans
        
