class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> stk;
        
        int i = 0, j;
        int n = heights.size();
        
        int ans = 0;
        while(i < n)
        {
            if(stk.empty() || heights[stk.top()] <= heights[i])
                stk.push(i), i++;
            
            else {
                j = stk.top();
                stk.pop(); 
                
                // empty means all those before this one is greater than this one.
                if(stk.empty())
                    ans = max(ans, heights[j] * i);
                
                // length from te popped element to i
                else
                    ans = max(ans, heights[j] * (i - stk.top() - 1));
            }
        }
        
        while(!stk.empty())
        {
            j = stk.top();
            stk.pop();
                
            // empty means all those before this one is greater than this one.
            if(stk.empty())
                ans = max(ans, heights[j] * i);
            
            // length from te popped element to i
            else
                ans = max(ans, heights[j] * (i - stk.top() - 1));  
        }
        
        return ans;
    }
};
