// Algorithm used - Topological Sort

class Solution {
public:
    vector<vector<int>> adj;
    vector<int> vis;
    bool cycle;

    void dfs(int src)
    {
        if(!vis[src])
        {
            vis[src] = 1;

            for(int i = 0; i < adj[src].size(); i++)
                dfs(adj[src][i]);

            vis[src] = 2;
        }

        else if(vis[src] == 1)
            cycle = true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        adj.resize(numCourses);
        vis.resize(numCourses);

        fill(vis.begin(), vis.end(), 0);
        cycle = false;

        for(int i = 0; i < prerequisites.size(); i++)
            adj[prerequisites[i][0]].push_back(prerequisites[i][1]);

        for(int i = 0; i < numCourses; i++)
        {
            if(!vis[i])
                dfs(i);
        }

        bool ans = true & !cycle;
        for(int i = 0; i < numCourses; i++)
        {
            if(!vis[i])
            {
                ans = false;
                break;
            }
        }

        return ans;
    }
};
