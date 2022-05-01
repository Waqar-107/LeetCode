class Solution {
public:
    int n, m;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    
    bool isInside(int r, int c) {
        return (r >= 0 && c >= 0 && r < n && c < m);
    }
    
    int dfs(int r, int c, vector<vector<int>>& matrix, vector<vector<int>>& cache) {
        if(cache[r][c]) return cache[r][c];

        for(int i = 0; i < 4; i++) {
            int x = dx[i] + r;
            int y = dy[i] + c;
            
            if(isInside(x, y) && matrix[x][y] > matrix[r][c])
                cache[r][c] = max(cache[r][c], dfs(x, y, matrix, cache));
        }
        
        return ++cache[r][c];
    }
    
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        n = matrix.size();
        m = matrix[0].size();
        
        vector<vector<int>> cache(n);
        for(int i = 0; i < n; i++) cache[i].resize(m);
        
        int ans = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                ans = max(ans, dfs(i, j, matrix, cache));
            }
        }
        
        return ans;
    }
};
