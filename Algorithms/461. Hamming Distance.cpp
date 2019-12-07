/***from dust i have come, dust i will be***/

class Solution {
public:
    int hammingDistance(int x, int y) {
        int cnt = 0;
        for(int i = 0; i < 32; i++){
            if((x & (1 << i)) ^ (y & (1 << i)))
                cnt++;
        }
        
        return cnt;
    }
};
