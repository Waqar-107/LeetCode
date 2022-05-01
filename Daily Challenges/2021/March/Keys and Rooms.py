class Solution:
    def __init__(self):
        self.vis = []
        
    
    def dfs(self, src, adj):
        self.vis[src] = True
        
        for node in adj[src]:
            if not self.vis[node]:
                self.dfs(node, adj)
        
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        self.vis = [False] * n
        
        self.dfs(0, rooms)
        
        for i in range(n):
            if not self.vis[i]:
                return False
        
        return True
