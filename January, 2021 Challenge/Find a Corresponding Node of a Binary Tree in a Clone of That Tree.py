# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        answer = None
    
    def solve(self, root, parent, target):
        if not root:
            return
        
        if root.val == target.val:
            self.answer = root
            return
        
        self.solve(root.left, root, target)
        self.solve(root.right, root, target)
            
            
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.solve(cloned, None, target)
        
        return self.answer
        
