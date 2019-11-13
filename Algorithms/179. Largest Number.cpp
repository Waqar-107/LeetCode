/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

bool cmp(string a, string b)
{
    return (a + b) > (b + a);
}

class Solution {
public:
    string intToStr(int x)
    {
        if(x == 0) return "0";

        string s;
        while(x)
        {
            s.push_back(x % 10 + '0');
            x /= 10;
        }

        reverse(s.begin(), s.end());
        return s;
    }
    
   
    
    string largestNumber(vector<int>& nums) {
        vector<string> vec;
        for(int e : nums)
            vec.push_back(intToStr(e));
        
        sort(vec.begin(), vec.end(), cmp);
            
        string ans = "";
        for(string e : vec) ans += e;
        
        // remove leading 0
        reverse(ans.begin(), ans.end());
        while(ans.size() && ans.back() == '0') ans.pop_back();
        reverse(ans.begin(), ans.end());
        
        if(ans.length() == 0 ) return "0";
        
        return ans;
    }
};
