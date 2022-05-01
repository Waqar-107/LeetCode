# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.trav = defaultdict(list)
        
    def solve(self, root, level):
        if not root:
            return
        
        self.trav[level].append(root.val)
        
        self.solve(root.left, level + 1)
        self.solve(root.right, level + 1)
        
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.solve(root, 0)
        
        ans = []
        for keys in self.trav:
            if keys % 2:
                ans.append(self.trav[keys][::-1])
            else:
                ans.append(self.trav[keys])
        
        return ans
