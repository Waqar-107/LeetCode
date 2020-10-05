class Solution {
public:
    int bitwiseComplement(int N) {
        long long int p = 1;
        int ans = 0;
        string s = "";
        
        for(int i = 0; i < 32; i++){
            if((N & (1 << i)) == 0)
                s.push_back('0');
            else s.push_back('1');
        }
        
        while(s.size() && s.back() == '0')
            s.pop_back();
        
        if(s.size() == 0) s.push_back('0');
        reverse(s.begin(), s.end());
        
        for(int i = s.size() - 1; i >= 0; i--)
            ans += p * (1 - s[i] + '0'), p *= 2;
        
        return ans;
    }
};
