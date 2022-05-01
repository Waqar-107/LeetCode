class Solution {
public:
    int cnt = 0;
    void solve(vector<int> &vec, int l)
    {
        if(l == vec.size())
            cnt++;
        
        for(int i = l; i < vec.size(); i++)
        {
            swap(vec[l], vec[i]);
            if(vec[l] % (l + 1) == 0 || (l + 1) % vec[l] == 0)
                solve(vec, l + 1);
            
            swap(vec[l], vec[i]);
        }
    }
    
    int countArrangement(int n) {
        vector<int> vec;
        for(int i = 1; i <= n; i++)
            vec.push_back(i);
        
        solve(vec, 0);
        return cnt;
    }
};
