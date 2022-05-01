# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.nodes = defaultdict(int)
    
    def solve(self, root, level):
        if not root:
            return
        
        self.cnt[level] += root.val
        self.nodes[level] += 1
        
        self.solve(root.left, level + 1)
        self.solve(root.right, level + 1)
        
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.solve(root, 1)
        
        ans = []
        for key in self.cnt:
            ans.append(self.cnt[key] / self.nodes[key])
        
        return ans
