/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";
        if(strs.size() == 0) return ans;
        
        int n = strs[0].length();
        for(int i = 0; i < n; i++){
           for(int j = 1; j < strs.size(); j++){
               if(strs[j].length() <= i) return ans;
               if(strs[j][i] != strs[0][i]) return ans;
           }
            
           ans.push_back(strs[0][i]);
        }
        
        return ans;
    }
};
