
/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

bool cmp(pair<string, string> a, pair<string, string> b){
    return a.first < b.first;
}

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<pair<string, string>> vec;
        string temp;
            
        for(string s : strs)
        {
            temp = s;
            sort(temp.begin(), temp.end());
            
            vec.push_back({temp, s});
        }
        
        sort(vec.begin(), vec.end());
        
        vector<vector<string>> ans;
        for(int i = 0; i < vec.size();){
            vector<string> temp;
            temp.push_back(vec[i].second);
            
            int k = i + 1;
            for(int j = i + 1; j < vec.size(); j++){
                if(vec[i].first == vec[j].first) {
                    k = j + 1;
                    temp.push_back(vec[j].second);
                }
                
                else {
                    k = j;
                    break;
                }
            }
            
            i = k;
            ans.push_back(temp);
        }
        
        return ans;
    }
};
