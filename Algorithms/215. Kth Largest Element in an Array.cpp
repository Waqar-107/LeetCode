/***from dust i have come, dust i will be***/

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end(), greater<>());
        return nums[k - 1];
    }
};
