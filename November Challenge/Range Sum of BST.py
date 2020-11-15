# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        
    def solve(self, root, lo, hi):
        if not root:
            return
        
        if lo <= root.val <= hi:
            self.sum += root.val
        
        self.solve(root.left, lo, hi)
        self.solve(root.right, lo, hi)
        
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.solve(root, low, high)
        return self.sum
        
