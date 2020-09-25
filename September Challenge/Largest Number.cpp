bool cmp(string s, string t){
    return (s + t) > (t + s);
}

string toStr(int n){
    string s = "";
    if(n == 0) return "0";
    
    while(n)
    {
        s.push_back(n % 10 + '0');
        n /= 10;
    }
    
    reverse(s.begin(), s.end());
    
    return s;
}

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> vec;
        for(int e : nums) vec.push_back(toStr(e));
        
        sort(vec.begin(), vec.end(), cmp);
        
        string ans = "";
        for(string s : vec) ans += s;
        
        for(int i = 0; i < ans.length(); i++){
            if(ans[i] != '0') return ans;
        }
        
        return "0";
    }
};
