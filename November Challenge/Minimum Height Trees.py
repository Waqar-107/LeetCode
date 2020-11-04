class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        adj = [set() for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            
            adj[u].add(v)
            adj[v].add(u)
        

        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            
            for leaf in leaves:
                for neighbor in adj[leaf]:
                    adj[neighbor].remove(leaf)
                    if len(adj[neighbor]) == 1:
                        new_leaves.append(neighbor)
            
            leaves = new_leaves
        
        return leaves
