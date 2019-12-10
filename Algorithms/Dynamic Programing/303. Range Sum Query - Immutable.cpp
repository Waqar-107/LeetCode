/***from dust i have come, dust i will be***/

class NumArray {
public:
    int *pre;
    NumArray(vector<int>& nums) {
        pre = new int[nums.size() + 1];
        
        pre[0] = 0;
        for(int i = 1; i <= nums.size(); i++)
            pre[i] = pre[i - 1] + nums[i - 1];
    }
    
    int sumRange(int i, int j) {
        return pre[j + 1] - pre[i];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
