/***from dust i have come, dust i will be***/

class Solution {
public:
    bool isPalindrome(string s)
    {
        int n = s.size();
        int i = 0, j = n - 1;
        
        while(i < j)
        {
            if(s[i] != s[j]) return false;
            i++, j--;
        }
        
        return true;
    }
    
    bool validPalindrome(string s) {
        int n = s.size();
        int i = 0, j = n - 1;
        int xi = -1, xj = -1;
        
        while(i < j)
        {
            if(s[i] != s[j]){
                xi = i;
                xj = j;
                break;
            }
            
            i++, j--;
        }
        
        if(xi == -1) return true;
        
        string x1, x2;
        for(i = 0; i < n; i++)
        {
            if(i != xi)
                x1.push_back(s[i]);
            if(i != xj)
                x2.push_back(s[i]);
        }
        
        return isPalindrome(x1) | isPalindrome(x2);
    }
};
