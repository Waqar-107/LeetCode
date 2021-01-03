# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = math.inf
    
    def dfs(self, node, level):
        if node == None:
            return
        
        if node.left == None and node.right == None:
            self.ans = min(self.ans, level)
        
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)
        
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        self.dfs(root, 1)
        return self.ans
        
