# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def solve(self, root, level):
        if not root:
            return
        
        if len(self.ans) < level:
            self.ans.append(-math.inf)
        
        self.ans[level - 1] = max(self.ans[level - 1], root.val)
        
        self.solve(root.left, level + 1)
        self.solve(root.right, level + 1)
        
    def largestValues(self, root: TreeNode) -> List[int]:
        self.solve(root, 1)
        return self.ans
