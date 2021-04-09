class Solution {
public:
    map<char, int> ordering;
    
    // return -1 if a < b, 0 if a == b, 1 if a > b
    int compare(string a, string b) {
        bool smaller = true;
        
        int len = min((int)a.length(), (int)b.length());
        
        for(int i = 0; i < len; i++)
        {
            if(ordering[a[i]] == ordering[b[i]]) continue;
            
            if(ordering[a[i]] < ordering[b[i]]) {
                return -1;
            }
            
            return 1; 
        }
        
        // at this point the len part are same
        // so if they are of the same length then send 0
        // else the longer string will be considered greater
        if(a.length() == b.length()) return 0;
        if(a.length() < b.length()) return -1;
        return 1;
    }
    
    bool isAlienSorted(vector<string>& words, string order) {
        for(int i = 0; i < order.length(); i++)
            ordering[order[i]] = i;
        
        for(int i = 1; i < words.size(); i++) {
            if(compare(words[i], words[i - 1]) > -1) continue;
            return false;
        }
        
        return true;
    }
};
