/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        int mp[1010] = {};
  
        for(int i = 0; i < arr1.size(); i++)
            mp[arr1[i]]++;
        
        
        vector<int> ans;
        for(int i = 0; i < arr2.size(); i++)
        {
            while(mp[arr2[i]]--)
                ans.push_back(arr2[i]);
        }
        
        for(int i = 0; i < 1010; i++)
        {
            while(mp[i] > 0) 
                ans.push_back(i), mp[i]--;
        }
        
        return ans;
    }
};
