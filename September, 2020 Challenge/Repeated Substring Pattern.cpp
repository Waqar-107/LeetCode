class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.length();
        int sq = sqrt(n * 1.0);
        
        vector<int> factors;
        for(int i = 1; i <= sq; i++)
        {
            if(n % i == 0)
            {
                factors.push_back(i);
                factors.push_back(n / i);
            }
        }
        
        int q;
        for(int e : factors)
        {
            // substr of length e copied q times 
            q = n / e;
            
            string temp = "";
            for(int i = 0; i < e; i++) temp.push_back(s[i]);
            
            string fin = "";
            for(int i = 0; i < q; i++) fin += temp;
            
            if(fin == s && n != e) return true;
        }
        
        return false;
    }
};
