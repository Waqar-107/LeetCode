/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        int i, j, k;
        int n = s.length();
        int m = t.length();
        
        vector<int> sv(300, 0);
        vector<int> tv(300, 0);
        
        for(i = 0; i < m; i++)
            tv[t[i]]++;
        
        i = 0, j = 0;
        int ans = n, ai = -1, aj = - 1;
        bool flag;
        
        while(j < n)
        {
            sv[s[j]]++;
            
            // check if i can move forward
            while(i < n)
            {
                if(!tv[s[i]]) 
                    sv[s[i]]--, i++;
                else if(tv[s[i]] && sv[s[i]] - 1 >= tv[s[i]]) 
                    sv[s[i]]--, i++;
                else 
                    break;
            }
               
            
            flag = true;
            for(k = 0; k < 300; k++)
            {
                if(tv[k] && sv[k] < tv[k]){
                    flag = false;
                    break;
                }
            }
            
            if(flag)
            {
                // cout << i << " " << j << endl;
                if(ans >= j - i + 1)
                {
                    ans = j - i + 1;
                    ai = i;
                    aj = j;
                }
            }
            
            j++;
        }
        
        string ret = "";
        if(ai == -1 || aj == -1) return ret;
        
        for(i = ai; i <= aj; i++)
            ret.push_back(s[i]);
        
        return ret;
    }
};
