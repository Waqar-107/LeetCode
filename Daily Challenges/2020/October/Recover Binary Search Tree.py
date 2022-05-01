# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.q = []
        
    def traverse(self, root, assign):
        if root == None:
            return
        
        self.traverse(root.left, assign)
        
        if not assign:
            self.q.append(root.val)
        else:
            root.val = self.q.pop(0)
        
        self.traverse(root.right, assign)
        
    def recoverTree(self, root: TreeNode) -> None:
        self.traverse(root, False)
        self.q.sort()
        self.traverse(root, True)
                    
                    
        
