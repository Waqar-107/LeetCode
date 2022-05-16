class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        
        if(grid[0][0]) return -1;
        
        int dist[n][m];
        bool vis[n][m];
        
        fill_n(&dist[0][0], n * m, INT_MAX);
        memset(vis, 0, sizeof(vis));
        
        queue<pair<int, int>> q;
        q.push({ 0, 0 });
        dist[0][0] = 0;
        vis[0][0] = true;
        
        int dx[] = {0, 0, 1, -1, -1, -1, 1, 1};
        int dy[] = {1, -1, 0, 0, -1, 1, 1, -1};
        
        while(!q.empty())
        {
            pair<int, int> u = q.front();
            q.pop();
            
            for(int i = 0; i < 8; i++)
            {
                int x = dx[i] + u.first;
                int y = dy[i] + u.second;
                
                if(x >= 0 && y >= 0 && x < n && y < m && !vis[x][y] && !grid[x][y] && dist[x][y] > dist[u.first][u.second] + 1)
                {
                    dist[x][y] = dist[u.first][u.second] + 1;
                    q.push({ x, y });
                    vis[x][y] = true;
                }
            }
        }
        
        if(!vis[n - 1][m - 1])
            return -1;
        
        return dist[n - 1][m - 1] + 1;
    }
};
