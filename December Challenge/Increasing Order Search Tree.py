# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mp = defaultdict(TreeNode)
        self.keys = []
    
    def traverse(self, root):
        if not root:
            return
        
        self.mp[root.val] = root
        
        self.traverse(root.left)
        
        self.keys.append(root.val)
        
        self.traverse(root.right)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        self.traverse(root)
        #print(self.keys)
        
        for i in range(len(self.keys) - 1):
            self.mp[self.keys[i]].left = None
            self.mp[self.keys[i]].right = self.mp[self.keys[i + 1]]
        
        self.mp[self.keys[-1]].left = None
        
        return self.mp[self.keys[0]]
