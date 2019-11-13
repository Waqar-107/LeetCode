/***from dust i have come, dust i will be***/

class Solution {
public:
    bool isPowerOfThree(int n) {
        while(n % 3 == 0 && n)
            n /= 3;
        
        if(n == 1) return true;
        return false;
    }
};
