/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        
        int i, n;
        int arr[300];
        memset(arr, 0, sizeof(arr));
        
        n = J.length();
        for(i = 0; i < n; i++)
            arr[J[i]]++;
        
        int cnt = 0;
        n = S.length();
        for(i = 0; i < n; i++)
        {
            if(arr[S[i]])
                cnt++;
        }
        
        return cnt;
    }
};