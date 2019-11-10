/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0) return 1.0;
        if(n == 1) return x;
        if(n == -1) return (1 / x);
        
        if(n % 2 == 0)
        {
            double t = myPow(x, n >> 1);
            return t * t;
        }
        
        // x ^ 5 = x ^ 4 * x
        if(n > 0)
        {
            double t = myPow(x, (n - 1));
            return t * x;
        }
        
        // x ^ -5 = x ^ -4 * x ^ - 1
        else
        {
            double t = myPow(x, (n + 1));
            return t * (1 / x);
        }
        
    }
};