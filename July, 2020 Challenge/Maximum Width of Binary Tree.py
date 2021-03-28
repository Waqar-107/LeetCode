# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vals = defaultdict(list)
    
    def solve(self, root, level, val):
        if not root:
            return
        
        self.vals[level].append(val)
        
        self.solve(root.left, level + 1, 2 * val)
        self.solve(root.right, level + 1, 2 * val + 1)
        
        
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.solve(root, 1, 1)
        
        ans = 0
        for key in self.vals:
            mn = min(self.vals[key])
            mx = max(self.vals[key])
            
            ans = max(ans, mx - mn + 1)
            
        return ans
