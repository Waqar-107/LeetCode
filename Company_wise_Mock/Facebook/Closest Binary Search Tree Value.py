# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = math.inf
        
    def solve(self, root, target):
        if not root:
            return
        
        if abs(target - self.ans) > abs(root.val - target):
            self.ans = root.val
        
        self.solve(root.left, target)
        self.solve(root.right, target)
    
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.solve(root, target)
        return self.ans
