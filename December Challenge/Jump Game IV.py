class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        vis = [False] * n
        adj = defaultdict(list)
        
        for i in range(n):
            adj[arr[i]].append(i)
        
        q = [0]
        vis[0] = True
        step = 0
        
        while len(q):
            nex = []
            
            for node in q:
                if node == n - 1:
                    return step
            
                for child in adj[arr[node]]:
                    if not vis[child]:
                        vis[child] = True
                        nex.append(child)
                
                adj[arr[node]].clear()
            
                if node + 1 < n and not vis[node + 1]:
                    nex.append(node + 1)
                    vis[node + 1] = True

                if node - 1 >= 0 and not vis[node - 1]:
                    nex.append(node - 1)
                    vis[node - 1] = True
            
            q = nex
            step += 1

        
        return -1
                
