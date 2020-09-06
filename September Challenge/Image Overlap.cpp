class Solution {
public:
    int mat[35][35];
    int match(vector<vector<int>>& B){
        int cnt = 0;
        for(int i = 0; i < B.size(); i++){
            for(int j = 0; j < B[0].size(); j++){
                if(mat[i][j] == B[i][j] && B[i][j]) cnt++;
            }
        }
        
        return cnt;
    }
    
    int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
        if(!A.size()) return 0;

        int n = A.size();
        int m = A[0].size();
        int cnt, mx = 0;

        // right
        for(int j = 0; j < m; j++)
        {
            // up
            for(int i = 0; i < n; i++)
            {
                memset(mat, 0, sizeof(mat));
                
                // check
                for(int r = 0; r < n - i; r++)
                {
                    for(int c = j; c < m; c++)
                        mat[r][c] = A[r + i][c - j];
                }

                mx = max(mx, this->match(B));
            }

            // down
            for(int i = 0; i < n; i++)
            {
                memset(mat, 0, sizeof(mat));
                
                // check
                for(int r = i; r < n; r++)
                {
                    for(int c = j; c < m; c++)
                        mat[r][c] = A[r - i][c - j];
                }

                mx = max(mx, this->match(B));
            }
        }
        
        // left
        for(int j = 0; j < m; j++)
        {
            // up
            for(int i = 0; i < n; i++)
            {
                memset(mat, 0, sizeof(mat));
                
                // check
                for(int r = 0; r < n - i; r++)
                {
                    for(int c = 0; c < m - j; c++)
                        mat[r][c] = A[r + i][c + j];
                }

                mx = max(mx, this->match(B));
            }

            // down
            for(int i = 0; i < n; i++)
            {
                memset(mat, 0, sizeof(mat));
                
                // check
                for(int r = i; r < n; r++)
                {
                    for(int c = 0; c < m - j; c++)
                        mat[r][c] = A[r - i][c + j];
                }

                mx = max(mx, this->match(B));
            }
        }

        return mx;
    }
};
