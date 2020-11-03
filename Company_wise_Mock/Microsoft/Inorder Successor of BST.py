# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        self.setAns = False
    
    def solve(self, root, target, left):
        if root == None:
            return
        
        if target == root:
            self.setAns = True
            return
            
        self.solve(root.left, target, True)
        if self.ans == None and self.setAns:
            self.ans = root
            
        self.solve(root.right, target, False)
             
      
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # if p.right is not null then leftmost of right subtree is answer
        # else find the one ancestor that is the left child
        if p.right:
            ans = p.right
            while ans.left:
                ans = ans.left
            
            return ans
        
        self.solve(root, p, True)
        return self.ans
