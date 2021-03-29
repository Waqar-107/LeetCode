# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root: TreeNode, container: List):
        if not root:
            return
        
        container.append(root.val)
        
        if root.left:
            self.solve(root.left, container)
        else:
            container.append(-math.inf)
            
        if root.right:
            self.solve(root.right, container)
        else:
            container.append(-math.inf)
            
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pc = []
        qc = []
        
        self.solve(p, pc)
        self.solve(q, qc)
        
        return pc == qc
        
