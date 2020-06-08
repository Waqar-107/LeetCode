/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> mp;
        
        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;
        
        int total = 0;
        for(int i = 0; i < s.length(); i++){
            total += mp[s[i]];
            
            if((s[i] == 'V' || s[i] == 'X') && i - 1 >= 0 && s[i - 1] == 'I') total -= 2;
            else if((s[i] == 'L' || s[i] == 'C') && i - 1 >= 0 && s[i - 1] == 'X') total -= 20;
            else if((s[i] == 'D' || s[i] == 'M') && i - 1 >= 0 && s[i - 1] == 'C') total -= 200;
        }
        
        return total;
    }
};
