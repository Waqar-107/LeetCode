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
    
    def determine_depth(self, root, d):
        if not root:
            return
        
        self.depth = max(self.depth, d)
        
        self.determine_depth(root.left, d + 1)
        self.determine_depth(root.right, d + 1)
    
    def determine_left_right_most(self, root, d):
        if not root:
            return
        
        if d == self.depth:
            if self.L == None:
                self.L = root
            else:
                self.R = root
        
        if root.left:
            self.parent[root.left.val] = root
            self.determine_left_right_most(root.left, d + 1)
        if root.right:
            self.parent[root.right.val] = root
            self.determine_left_right_most(root.right, d + 1)
        
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.determine_depth(root, 0)
        self.determine_left_right_most(root, 0)
        
        if not self.L and not self.R:
            return root
        if self.L and not self.R:
            return self.L
        
        while True:
            if self.parent[self.L.val] == self.parent[self.R.val]:
                return self.parent[self.L.val]
            
            self.L = self.parent[self.L.val]
            self.R = self.parent[self.R.val]
        
