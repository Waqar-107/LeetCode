/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    string reverseOnlyLetters(string S) {
        string ret = S;
        vector<char> vec;
        
        int i, n = S.length();
        for(int i = 0; i < n; i++)
        {
            if(isalpha(S[i]))
                vec.push_back(S[i]);
        }
        
        int k = 0;
        for(i = n - 1; i >= 0; i--)
        {
            if(isalpha(S[i]))
                ret[i] = vec[k++];
        }
        
        return ret;
    }
};
