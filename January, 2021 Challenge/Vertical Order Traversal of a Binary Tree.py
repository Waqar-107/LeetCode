# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.trav = defaultdict(list)
    
    def solve(self, root, x, y):
        if not root:
            return
        
        self.trav[x].append((y, root.val))
        self.solve(root.left, x - 1, y - 1)
        self.solve(root.right, x + 1, y - 1)
        
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.solve(root, 0, 0)
        
        ans = []
        keys = list(self.trav.keys())
        keys.sort()
        
        for key in keys:
            self.trav[key].sort(key=lambda x: (-x[0], x[1]))
            temp = []
            for e in self.trav[key]:
                temp.append(e[1])
            
            ans.append(temp)
        
        return ans
        
