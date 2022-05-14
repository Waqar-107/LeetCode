struct node {
    int at, cost;
    node(){}
    node(int at, int cost)
    {
        this->at = at;
        this->cost = cost;
    }
};

struct edge {
    int v, w;
    edge(){}
    edge(int v, int w)
    {
        this->v = v;
        this->w = w;
    }
};

class comparator
{
public:
    bool operator() (node a, node b)
    {
       return a.cost > b.cost;
    }
};

class Solution {
public:
    int dijkstra(int n, int k, vector<vector<edge>> adj)
    {
        vector<bool> vis(n + 1, false);
        vector<int> dist(n + 1, INT_MAX);
        
        priority_queue<node, vector<node>, comparator> pq;
        
        dist[k] = 0;
        pq.push(node(k, 0));
        
        while(!pq.empty())
        {
            node u = pq.top();
            pq.pop();
            
            if(vis[u.at])
                continue;
            
            for(edge e : adj[u.at])
            {
                if(!vis[e.v] && dist[e.v] > dist[u.at] + e.w)
                {
                    dist[e.v] = dist[u.at] + e.w;
                    pq.push(node(e.v, dist[e.v]));
                }
            }
            
            vis[u.at] = true;
        }
        
        int mx = 0;
        for(int i = 1; i <= n; i++)
        {
            if(!vis[i]) return -1;
            
            if(i != k) {
                mx = max(mx, dist[i]);
            }
        }
        
        return mx;
    }
    
    
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<edge>> adj(n + 1);
        for(int i = 0; i < times.size(); i++)
            adj[times[i][0]].push_back(edge(times[i][1], times[i][2]));
        
        return dijkstra(n, k, adj);
    }
};
