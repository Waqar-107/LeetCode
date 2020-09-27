class Solution:
    def __init__(self):
        self.graph = {}
        self.vis = {}
        self.ans = 0
    
    def dfs(self, src, target, val):
        if src == target:
            self.ans = val
        
        self.vis[src] = True
        
        if src in self.graph:
            for node in self.graph[src]:
                if node[0] not in self.vis:
                    # print("from", src, "to", node[0])
                    self.dfs(node[0], target, node[1] * val)
                
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        i = 0
        for eq in equations:
            if eq[0] not in self.graph:
                self.graph[eq[0]] = []
            if eq[1] not in self.graph:
                self.graph[eq[1]] = []
            
            self.graph[eq[0]].append((eq[1], values[i]))
            self.graph[eq[1]].append((eq[0], 1.0 / values[i]))
            i += 1
        
        ret = []
        print(self.graph)
        for q in queries:
            self.ans = -1.0
            
            if q[0] == q[1]:
                if q[0] in self.graph:
                    self.ans = 1.0
            
            else:
                self.vis = {}
                self.dfs(q[0], q[1], 1.0)
            
            ret.append(self.ans)
        
        
        return ret
                
            
            
