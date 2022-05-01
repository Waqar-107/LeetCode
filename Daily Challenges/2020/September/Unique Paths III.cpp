class Solution {
public:
    int n, m, cnt, total, visSoFar;
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};
    bool vis[25][25];
    
    bool inside(int r, int c) {
        return (r >= 0 && c >= 0 && r < n && c < m);
    }
    
    void dfs(int r, int c, vector<vector<int>>& grid)
    {
        if(grid[r][c] == 2) {
            // exclude this cell, so total - 1
            if(visSoFar == total - 1)
                cnt++;
            
            return;
        }
        
        visSoFar++;
        vis[r][c] = true;
        
        for(int i = 0; i < 4; i++){
            int x = r + dx[i];
            int y = c + dy[i];
            
            
            if(inside(x, y) && grid[x][y] != -1 && !vis[x][y]) dfs(x, y, grid);
        }
        
        visSoFar--;
        vis[r][c] = false;
    }
    
    int uniquePathsIII(vector<vector<int>>& grid) {
        n = grid.size();
        if(!n) return 0;
        m = grid[0].size();
        
        int sr, sc;
        
        total = 0;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++){
                if(grid[i][j] != -1) total++;
                
                if(grid[i][j] == 1) sr = i, sc = j;
            }
        }
        
        cnt = 0; visSoFar = 0;
        memset(vis, 0, sizeof(vis));
        dfs(sr, sc, grid);
        
        return cnt;
    }
};
