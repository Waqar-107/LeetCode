/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        string morse[] = {".-","-...","-.-.","-..",".","..-.",
                          "--.","....","..",".---","-.-",
                          ".-..","--","-.","---",".--.",
                          "--.-",".-.","...","-","..-",
                          "...-",".--","-..-","-.--","--.."};
        
        unordered_map<string, int> mp;
        for(string s : words)
        {
            string trans = "";
            for(int i = 0; i < s.length(); i++)
                trans += morse[s[i] - 'a'];
            
            mp[trans]++;
        }
        
        return mp.size();
    }
};
