/***from dust i have come, dust i will be***/

class Solution {
public:
    string toLowerCase(string str) {
        for(int i = 0; i < str.length(); i++)
            str[i] = tolower(str[i]);
            return str;
    }
};
