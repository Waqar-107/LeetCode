class Solution {
public:
    void sortColors(vector<int>& nums) {
        int cnt[3] = {0, 0, 0};
        for(int e : nums){
            cnt[e]++;
        }
        
        int idx = 0;
        for(int j = 0; j < 3; j++)
        {
            for(int i = 0; i < cnt[j]; i++)
                nums[idx] = j, idx++;
        }
    }
};
