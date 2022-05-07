class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n2 = INT_MIN;
        stack<int> n3Container;
        
        for(int i = nums.size() - 1; i >= 0; i--) {
            if(nums[i] < n2) {
                return true;
            }
            
            while(!n3Container.empty() && n3Container.top() < nums[i]) {
                n2 = n3Container.top();
                n3Container.pop();
            }
            
            n3Container.push(nums[i]);
        }
        
        return false;
    }
};
