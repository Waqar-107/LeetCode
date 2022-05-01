# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.pre = []
        self.idx = 1
        
    def solve(self, root, voyage):
        if not root:
            return
        
        self.pre.append(root.val)
        
        flag = False
        if root.left:
            if root.left.val != voyage[self.idx] and root.right:
                self.idx += 1
                self.solve(root.right, voyage)
                flag = True
                self.ans.append(root.val)
                
            self.idx += 1
            self.solve(root.left, voyage)
        
        if root.right and not flag:
            self.idx += 1
            self.solve(root.right, voyage)
                
            
        
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        if root.val != voyage[0]:
            return [-1]
        
        self.solve(root, voyage)
        
        if voyage != self.pre:
            return [-1]
        
        return self.ans
