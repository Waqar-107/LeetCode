/***from dust i have come, dust i will be***/

class Solution {
public:
    int balancedStringSplit(string s) {
        int i, n = s.length(), R = 0, cnt = 0;
        for(i = 0; i < n; i++){
            if(s[i] == 'R'){
                R++;
                
                if(R == 0) cnt++;
            }
            else
            {
                R--;
                if(R == 0) cnt++;
            }
        }
        
        return cnt;
    }
};
