# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, depth, v, d, left, parent):
        if d == depth:
            if left:
                newNode = TreeNode(v, root, None)
                parent.left = newNode
            else:
                newNode = TreeNode(v, None, root)
                parent.right = newNode
            
            return
        
        if root.left:
            self.solve(root.left, depth + 1, v, d, True, root)
        
        if root.right:
            self.solve(root.right, depth + 1, v, d, False, root)
            
        if not root.left and depth == d - 1:
            root.left = TreeNode(v)
        
        if not root.right and depth == d - 1:
            root.right = TreeNode(v)
                
            
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            newNode = TreeNode(v, root, None)
            return newNode
        
        self.solve(root, 1, v, d, 
                   False, None)
        return root
