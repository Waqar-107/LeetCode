class Solution {
public:
    vector<vector<int>> largeGroupPositions(string S) {
        int l = 0, r = 0;
        vector<vector<int>> vec;
        vector<int> temp;
        
        for(int i = 1; i < S.size(); i++){
          if(S[i] == S[i - 1]) r++;
          else {
              if(r - l + 1>= 3)
              {
                  temp.clear();
                  temp.push_back(l);
                  temp.push_back(r);
                  
                  vec.push_back(temp);
              }
              
              l = i, r = i;
          }
        }
        
        if(r - l + 1>= 3)
        {
            temp.clear();
            temp.push_back(l);
            temp.push_back(r);
                  
            vec.push_back(temp);
        }
        
        return vec;
    }
};
