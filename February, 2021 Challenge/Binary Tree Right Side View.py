# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mp = defaultdict(int)
        
    def solve(self, root, level):
        if not root:
            return
        
        self.mp[level] = root.val
        
        self.solve(root.left, level + 1)
        self.solve(root.right, level + 1)
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        self.solve(root, 1)
        
        for key in self.mp:
            ans.append(self.mp[key])
        
        return ans
