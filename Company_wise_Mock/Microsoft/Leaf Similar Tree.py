# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.uno = []
        self.dos = []
    
    def traverse(self, root, no):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            if no == 1:
                self.uno.append(root.val)
            else:
                self.dos.append(root.val)
        
        self.traverse(root.left, no)
        self.traverse(root.right, no)
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.traverse(root1, 1)
        self.traverse(root2, 2)
        
        return self.uno == self.dos
           
