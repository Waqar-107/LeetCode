class Solution:
    def __init__(self):
        self.color = []
        self.bipartite = True
    
    def dfs(self, src, col, graph):
        self.color[src] = col
        
        for v in graph[src]:
            if self.color[v] == -1:
                self.dfs(v, 1 - col, graph)
            else:
                if self.color[v] == col:
                    self.bipartite = False
                    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.color = [-1] * n
        
        for i in range(n):
            if self.color[i] == -1:
                self.dfs(i, 0, graph)
                
        return self.bipartite
        
        
