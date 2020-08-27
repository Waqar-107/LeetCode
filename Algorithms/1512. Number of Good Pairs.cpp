class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int cnt[101];
        memset(cnt, 0, sizeof(cnt));
        
        int n = nums.size();
        for(int i = 0; i < n; i++){
            cnt[nums[i]]++;
        }
        
        int sum = 0;
        for(int i = 0; i < 101; i++){
            sum += (cnt[i] * (cnt[i] - 1)) / 2;
        }
        
        return sum;
    }
};
