class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> result;
        
        for(int e : nums) {
            if(e % 2 == 0) {
                result.push_back(e);
            }
        }
        
        for(int e : nums) {
            if(e % 2) {
                result.push_back(e);
            }
        }
        
        return result;
    }
};
