/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<string> ans;
    vector<string> arr;
    
    void solve(string digits, int idx, string str)
    {
        if(digits.length() == idx){
            ans.push_back(str);
            return;
        }
        
        for(int i = 0; i < arr[digits[idx] - '0'].length(); i++){
            str.push_back(arr[digits[idx] - 48][i]);
            solve(digits, idx + 1, str);
            str.pop_back();
        }
    }
    
    vector<string> letterCombinations(string digits) {
        string temp[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        for(int i = 0; i < 10; i++) arr.push_back(temp[i]);
        
        if(digits.length() == 0) return ans;
        
        solve(digits, 0, "");
        return ans;
    }
};
