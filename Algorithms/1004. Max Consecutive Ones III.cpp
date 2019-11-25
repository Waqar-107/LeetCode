/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

class Solution {
public:
    int longestOnes(vector<int>& A, int k) {
        int i = 0, j = 0, n = A.size();
        int mx = 0, cnt = 0;
        
        while(j < n)
        {
            if(!A[j]) cnt++;
            
            if(cnt <= k){
                mx = max(mx, j - i + 1);
                j++;
            }
            
            else
            {
                while(i < j && cnt > k){
                    if(!A[i])cnt--;
                    i++;
                }
             
                j++;
            }
        }
        
        return mx;
    }
};
