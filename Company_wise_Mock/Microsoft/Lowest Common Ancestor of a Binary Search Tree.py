# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def traverse(self, root, p, q):
        if root == None:
            return
        
        if root.val < p.val and root.val < q.val:
            self.traverse(root.right, p, q)
        
        elif root.val > p.val and root.val > q.val:
            self.traverse(root.left, p, q)
        
        else:
            self.ans = root
            return
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.traverse(root, p, q)
        return self.ans
