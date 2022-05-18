#define pb push_back
#define pp pair<int, int>

class Graph
{
    int n, time;
    vector<vector<int>> adj;
    vector<pp> answer;

    void bridgeUtil(int current, int parent, vector<bool> &visited, vector<int> &discoveryTime, vector<int> &low)
    {
        visited[current] = true;
        discoveryTime[current] = time;
        low[current] = time;
        time++;

        for(int e : adj[current])
        {
            if(!visited[e])
            {
                bridgeUtil(e, current, visited, discoveryTime, low);

                // now parent will see if they can disconnect the edge between them and the child
                // if the child has any adjacent node other than the parent whose discovery time is less than parents discovery time
                // then we can safely assume that the child can be reached out using that node instead of using the parent node
                // thus the edge between the parent and the child is not a bridge
                low[current] = min(low[current], low[e]);
                if(low[e] > discoveryTime[current])
                    answer.pb({ current, e});
            }

            else if(e != parent)
                low[current] = min(low[current], discoveryTime[e]);
        }
    }
public:
    Graph(int n)
    {
        this->n = n;
        adj.resize(n + 1);      // keeping this 1 indexed
    }

    void addEdge(int u, int v)
    {
        adj[u].pb(v);
        adj[v].pb(u);
    }

    vector<pp> bridge()
    {
        vector<bool> visited(n + 1, false);
        vector<int> discoveryTime(n + 1);
        vector<int> low(n + 1);

        time = 1;
        answer.clear();

        for(int i = 1; i <= n; i++)
        {
            if(!visited[i])
                bridgeUtil(i, -1, visited, discoveryTime, low);
        }

        return answer;
    }
};

class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        Graph g(n);
        
        for(int i = 0; i < connections.size(); i++)
        {
            // add 1 as the Graph class is 1-indexed
            g.addEdge(connections[i][0] + 1, connections[i][1] + 1);
        }
        
        vector<pp> ans = g.bridge();
        vector<vector<int>> ret;
        
        for(pp edge : ans)
        {
            ret.pb(vector<int> { edge.first - 1, edge.second - 1 });
        }
        
        return ret;
    }
};
