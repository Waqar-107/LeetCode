# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = -1
        self.parent = defaultdict(TreeNode)
        self.L = None
        self.R = None
    
    def depthCalc(self, root, d):
        if not root:
            return
        
        self.depth = max(self.depth, d)
        
        if root.left:
            self.parent[root.left.val] = root
            self.depthCalc(root.left, d + 1)
        
        if root.right:
            self.parent[root.right.val] = root
            self.depthCalc(root.right, d + 1)
        
    def solve(self, root, d):
        if not root:
            return
        
        if self.depth == d:
            if self.L == None:
                self.L = root
            else:
                self.R = root
        
        self.solve(root.left, d + 1)
        self.solve(root.right, d + 1)
        
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.depthCalc(root, 0)
        self.solve(root, 0)
        
        if root == None:
            return root
        
        if root.left == None and root.right == None:
            return root
        
        if self.R == None:
            return self.L
        
        # return LCA of L and R
        while True:
            if self.parent[self.L.val] == self.parent[self.R.val]:
                return self.parent[self.L.val]
            
            self.L = self.parent[self.L.val]
            self.R = self.parent[self.R.val]
        
