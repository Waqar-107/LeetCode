class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vis = {}
    
    def dfs(self, src):
        self.vis[src] = True
        for e in self.graph[src]:
            if e not in self.vis:
                self.dfs(e)
        
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        for i in range(n):
            if i + arr[i] < n:
                self.graph[i].append(i + arr[i])
            if i - arr[i] >= 0:
                self.graph[i].append(i - arr[i])
        
        self.dfs(start)
        
        for i in range(n):
            if arr[i] == 0 and i in self.vis:
                return True
        
        return False
