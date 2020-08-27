class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        int ri, rj;
        for(int i = 0; i < 8; i++)
        {
            for(int j = 0; j < 8; j++){
                if(board[i][j] == 'R'){
                    ri = i;
                    rj = j;
                }
            }
        }
     
        int cnt = 0;
        
        // up
        for(int i = ri - 1; i >= 0; i--){
            if(board[i][rj] == 'B') break;
            if(board[i][rj] == 'p') {
                cnt++;
                break;
            }
        }
        
        // down
        for(int i = ri + 1; i < 8; i++){
            if(board[i][rj] == 'B') break;
            if(board[i][rj] == 'p') {
                cnt++;
                break;
            }
        }
        
        // right
        for(int j = rj + 1; j < 8; j++){
            if(board[ri][j] == 'B') break;
            if(board[ri][j] == 'p') {
                cnt++;
                break;
            }
        }
        
        // left
         for(int j = rj - 1; j >= 0; j--){
            if(board[ri][j] == 'B') break;
            if(board[ri][j] == 'p') {
                cnt++;
                break;
            }
        }
        
        return cnt;
    }
};
