class Solution:
    def __init__(self):
        self.hasCycle = False
        
    def dfs(self, src, vis, graph, ans):
        vis[src] = 1
          
        for node in graph[src]:
            if vis[node] == 0:
                self.dfs(node, vis, graph, ans)
                
            # cycle
            elif vis[node] == 1:
                self.hasCycle = True
        
        vis[src] = 2
        ans.append(src)
                
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            indegree[pre[1]] += 1
            
        vis = [0] * numCourses
        
        canBeStart = []
        for i in range(numCourses):
            if indegree[i] == 0:
                canBeStart.append(i)
        
        ans = []
        for src in canBeStart:
            if not vis[src]:
                self.dfs(src, vis, graph, ans)
        
        if not self.hasCycle and len(ans) == numCourses:
            return ans
        
        return []
    
