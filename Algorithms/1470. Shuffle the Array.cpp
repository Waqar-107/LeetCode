class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        int i = 0, j = n;
        vector<int> vec;
        
        while(j < n * 2){
            vec.push_back(nums[i++]);
            vec.push_back(nums[j++]);
        }
        
        return vec;
    }
};
