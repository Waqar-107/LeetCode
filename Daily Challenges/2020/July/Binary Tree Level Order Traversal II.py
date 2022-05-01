# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = defaultdict(list)
    
    def solve(self, root, lvl):
        if not root:
            return 
        
        self.ans[lvl].append(root.val)
        
        self.solve(root.left, lvl + 1)
        self.solve(root.right, lvl + 1)
        
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        self.solve(root, 0)
        
        mx = max(self.ans.keys())
        ans = []
        
        for i in range(mx, -1, -1):
            ans.append(self.ans[i])
        
        return ans
