import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = []
        for i in range(N + 1):
            graph.append([])
            
        for g in times:
            graph[g[0]].append((g[2], g[1]))
        
        inf = 1000000000
        dist = [inf] * (N + 1)
        vis = [False] * (N + 1)
        pq = []
        
        heapq.heappush(pq, (0, K))
        dist[K] = 0
        
        while len(pq):
            u = heapq.heappop(pq)
            # print("in", u[1], vis[u[1]])
            
            if vis[u[1]]:
                continue
            
            for neighbors in graph[u[1]]:
                #print("neigh", neighbors, vis[neighbors[1]], dist[neighbors[1]], dist[u[1]] + neighbors[0])
                if not vis[neighbors[1]] and dist[neighbors[1]] > dist[u[1]] + neighbors[0]:
                    dist[neighbors[1]] = dist[u[1]] + neighbors[0]
                    heapq.heappush(pq, (dist[neighbors[1]], neighbors[1]))
            
            vis[u[1]] = True
        
        for i in range(1, N + 1, 1):
            if vis[i] == False:
                return -1
        
        return max(dist[1:])
