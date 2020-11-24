# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    
    def solve(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        left = self.solve(root.left)
        right = self.solve(root.right)
        
        self.ans = max(left + right, self.ans)
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.solve(root)
        return self.ans
