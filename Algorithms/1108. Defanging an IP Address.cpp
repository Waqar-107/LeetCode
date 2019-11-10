/***from dust i have come, dust i will be***/
#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    string defangIPaddr(string address) {
        string s;
        for(int i = 0; i < address.length(); i++)
        {
            if(address[i] == '.')
                s += "[.]";
            else
                s.push_back(address[i]);
        }
        
        return s;
    }
};


