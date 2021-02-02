# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_root(self, root, lo, hi):
        if root == None:
            return
        
        if lo <= root.val <= hi:
            return root
        
        if root.val < lo:
            return self.find_root(root.right, lo, hi)

        else:
            return self.find_root(root.left, lo, hi)
    
    def solve(self, root, lo, hi):
        if root == None:
            return
        
        if root.left:
            if lo <= root.left.val <= hi:
                self.solve(root.left, lo, hi)
            else:
                # cut off the left subtree of root.left
                # root.left.right is still under consideration
                root.left = root.left.right
                self.solve(root, lo, hi)
        
        if root.right:
            if lo <= root.right.val <= hi:
                self.solve(root.right, lo, hi)
            else:
                # cut off the right subtree of root.right
                # root.right.left is still under consideration
                root.right = root.right.left
                self.solve(root, lo, hi)
                    
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        ans_root = self.find_root(root, low, high)
        self.solve(ans_root, low, high)
        
        return ans_root
        
        
