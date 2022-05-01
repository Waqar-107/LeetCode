# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, parents_key):
        if not root:
            return 0
        
        r = self.solve(root.right, parents_key)
        l = self.solve(root.left, root.val + r + parents_key)

        rv = root.val
        root.val += (r + parents_key)
        
        return r + l + rv
        
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.solve(root, 0)
        return root
