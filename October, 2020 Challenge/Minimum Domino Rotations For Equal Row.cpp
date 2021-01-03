class Solution {
public:
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        int mn = A.size() + 1, cnt;
        bool flag;
        
        for(int i = 1; i <= 6; i++)
        {
            // suppose A is the target
            flag = true;
            cnt = 0;
            for(int j = 0; j < A.size(); j++)
            {
                if(A[j] == i)
                    continue;
                
                if(B[j] == i) cnt++;
                else {
                    flag = false;
                    break;
                }
            }
            
            if(flag) mn = min(mn, cnt);
            
            // suppose B is the target
            flag = true;
            cnt = 0;
            for(int j = 0; j < A.size(); j++)
            {
                if(B[j] == i)
                    continue;
                
                if(A[j] == i) cnt++;
                else {
                    flag = false;
                    break;
                }
            }
            
            if(flag) mn = min(mn, cnt);
        }
        
        if(mn > A.size()) return -1;
        return mn;
    }
};
