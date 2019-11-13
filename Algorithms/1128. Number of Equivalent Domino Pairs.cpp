/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        int arr[10][10] = {};
        for(vector vec : dominoes)
        {
            if(vec[0] > vec[1])
                swap(vec[0], vec[1]);
            
            arr[vec[0]][vec[1]]++;
        }
        
        int ans = 0;
        for(int i = 1; i <= 9; i++)
        {
            for(int j = 1; j <= 9; j++)
            {
                if(arr[i][j])
                {
                    arr[i][j] = (arr[i][j] - 1) * arr[i][j];
                    ans += arr[i][j] / 2;
                }
            }
        }
        
        return ans;
    }
};
