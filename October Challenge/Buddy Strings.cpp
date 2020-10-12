class Solution {
public:
    bool buddyStrings(string A, string B) {
        vector<int> idx, cnt(26, 0);
        
        for(int i = 0; i < A.size(); i++){
            if(A[i] != B[i])
                idx.push_back(i);
            
            cnt[A[i] - 'a']++;
        }
        
        // identical strings
        if(idx.size() == 0){
            for(int i = 0; i < 26; i++){
                if(cnt[i] > 1) return true;
            }
            
            return false;
        }
        
        if(idx.size() == 2){
            swap(A[idx[0]], A[idx[1]]);
            if(A == B) return true;
        }
        
        return false;
        
    }
};
