"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.vis = {}
        self.ans = {}
    
    def dfs(self, root):
        if root == None or root.val in self.vis:
            return
        
        self.vis[root.val] = True
        self.ans[root.val] = Node(root.val, [])
        
        for n in root.neighbors:
            self.dfs(n)
        
    def solve(self, root):
        if root == None or root.val in self.vis:
            return
        
        self.vis[root.val] = True
        
        for n in root.neighbors:
            self.ans[root.val].neighbors.append(self.ans[n.val])
            self.solve(n)
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        self.dfs(node)
        self.vis = {}
        self.solve(node)
        
        return self.ans[node.val]
