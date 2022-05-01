class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        multiset<int> a;
        for(int e : A) a.insert(e);
        
        for(int i = 0; i < B.size(); i++) {
            auto itr = a.upper_bound(B[i]);
            if(itr == a.end())
                itr = a.begin();
            
            A[i] = *itr;
            a.erase(itr);
        }
        
        return A;
    }
};
